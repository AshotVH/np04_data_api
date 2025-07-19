from flask import Flask, request, jsonify, Response
from flask_cors import CORS
import requests
import os
import simplejson

app = Flask(__name__)


CORS(app)

API_ADDRESS = os.environ.get("API_ADDRESS")




@app.route('/np04cachedvals', methods=['GET'])
def np04cachedvals():
    args = request.args
    elemName = args.get('elemname')
    response = requests.get(f"{API_ADDRESS}/latest/{elemName}")
    data = response.json()
    json_data = simplejson.dumps(data, ignore_nan=True)
    return response
    return Response(json_data, content_type='application/json')


@app.route('/np04histogram/<elem_id>/<start_date>/<end_date>')
def np04histogram(start_date, end_date, elem_id):
    response = requests.get(f"{API_ADDRESS}/range/{start_date}/{end_date}/{elem_id}")
    data = response.json()
    json_data = simplejson.dumps(data, ignore_nan=True)
    return response
    return Response(json_data, content_type='application/json')

@app.route('/np04histogram_average/<elem_id>/<start_date>/<end_date>')
def np04histogram_average(start_date, end_date, elem_id):
    response  = requests.get(f"{API_ADDRESS}/average/{start_date}/{end_date}/{elem_id}")
    data = response.json()
    json_data = simplejson.dumps(data, ignore_nan=True)
    return response
    return Response(json_data, content_type='application/json')

@app.route('/sensorname/<elem_id>/')
def sensorname(elem_id):
    response = requests.get(f"{API_ADDRESS}/sensor-name/{elem_id}")
    data = response.json()
    json_data = simplejson.dumps(data, ignore_nan=True)
    return response
    return Response(json_data, content_type='application/json')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)