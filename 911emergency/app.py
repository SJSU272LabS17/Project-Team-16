from flask import Flask, render_template, request, make_response, flash, redirect, session, abort, jsonify
import json
from urllib.request import urlopen
from functions import *

app = Flask(__name__)
@app.route('/')
def index():
   return render_template('index.html')

@app.route('/bar')
def bar():
   return render_template('bar.html')

@app.route('/emergency', methods=['GET', 'POST'])
def emergency():
    if not request.json or not 'year' in request.json:
        abort(400)
    year = request.json['year']
    result = emergency_overview(year)
    return jsonify(result)

@app.route('/emergency_trend', methods=['GET', 'POST'])
def trend():
    if not request.json or not 'year' in request.json or not 'emergency_type' in request.json or not 'sub_emergency_type' in request.json:
        abort(400)
    year = request.json['year']
    emergency_type = request.json['emergency_type']
    sub_emergency_type = request.json['sub_emergency_type']
    result = emergency_trend(year, emergency_type, sub_emergency_type)
    return jsonify(result)

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

if __name__ == '__main__':
    app.run(debug = True)
