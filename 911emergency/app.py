from flask import Flask, render_template, request, make_response, url_for, flash, redirect, session, abort, jsonify
from flask_oauth import OAuth
import json
from urllib.request import urlopen
from urllib.request import urlopen, URLError, Request
from urllib.request import urlopen
from functions import *

app = Flask(__name__)

#home route
@app.route('/')
def index():
   return render_template('index.html')

#emergency type api
@app.route('/category', methods=['GET', 'POST'])
def type():
    result = emergency_type()
    return jsonify(result)

#emergency trend drop-down values api
@app.route('/sub_category', methods=['GET', 'POST'])
def trend_sub_dropdown():
    if not request.json or not 'emergency_type' in request.json or not 'year' in request.json:
        abort(400)
    year = request.json['year']
    emergency_type = request.json['emergency_type']
    result = type_trend_values(year,emergency_type)
    return jsonify(result)

#emergency overview api
@app.route('/emergency', methods=['GET', 'POST'])
def emergency():
    if not request.json or not 'year' in request.json:
        abort(400)
    year = request.json['year']
    result = emergency_overview(year)
    return jsonify(result)

#trend api
@app.route('/emergency_trend', methods=['GET', 'POST'])
def trend():
    if not request.json or not 'year' in request.json or not 'emergency_type' in request.json or not 'sub_emergency_type' in request.json:
        abort(400)
    year = request.json['year']
    emergency_type = request.json['emergency_type']
    sub_emergency_type = request.json['sub_emergency_type']
    result = emergency_trend(year, emergency_type, sub_emergency_type)
    return jsonify(result)

#comparison api
@app.route('/trend_comparison', methods=['GET', 'POST'])
def trend_comparison():
    if not request.json or not 'year' in request.json or not 'emergency_type' in request.json or not 'sub_emergency_type1' in request.json or not 'sub_emergency_type2' in request.json:
        abort(400)
    year = request.json['year']
    emergency_type = request.json['emergency_type']
    sub_emergency_type1 = request.json['sub_emergency_type1']
    sub_emergency_type2 = request.json['sub_emergency_type2']
    result = emergency_trend_comparison(year, emergency_type, sub_emergency_type1, sub_emergency_type2)
    return jsonify(result)

#heat map api
@app.route('/heat_map', methods=['GET', 'POST'])
def heat_map_generator():
    if not request.json or not 'year' in request.json:
        abort(400)
    year = request.json['year']
    result = heat_map(year)
    return jsonify(result)

#google_map api
@app.route('/google', methods=['GET'])
def google():
    result = google_map()
    return jsonify(result)

#median income api
@app.route('/income', methods=['GET'])
def income():
    result = income_trend()
    return jsonify(result)

#home value api
@app.route('/h_value', methods=['GET'])
def h_value():
    result = home_value()
    return jsonify(result)

#small business api
@app.route('/small_b', methods=['GET'])
def small_b():
    result = small_business()
    return jsonify(result)

#emergency expenditure api
@app.route('/expenditure', methods=['GET'])
def expenditure():
    result = emergency_expenditure()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug = True)
