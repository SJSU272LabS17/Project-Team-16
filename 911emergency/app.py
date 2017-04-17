from flask import Flask, render_template, request, make_response, flash, redirect, session, abort, jsonify
from pandas import *
import datetime as dt
import json
import os
from urllib.request import urlopen

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('test.html')

@app.route('/bar')
def bar():
   return render_template('bar.html')

@app.route('/emergency', methods=['GET', 'POST'])
def emergency():
    if request.method == 'POST' or request.method == 'GET':
        year = request.form.get('year_select')
        result = json.loads(emergency_overview(year))
        return jsonify(result)

# read 911 csv
cwd = os.getcwd() + '/' + 'montgomeryPA_911.csv'
data = read_csv(cwd)
pandas.to_datetime(data['timeStamp'])
def emergency_overview(year):
    overview_data = data[data['timeStamp'].str.contains(year)]
    overview_data_ems = overview_data[overview_data['title'].str.contains('EMS:')]
    overview_data_fire = overview_data[overview_data['title'].str.contains('Fire:')]
    overview_data_traffic = overview_data[overview_data['title'].str.contains('Traffic:')]
    count_ems = len(overview_data_ems.index)
    count_fire = len(overview_data_fire.index)
    count_traffic = len(overview_data_traffic.index)
    dictionary = {"EMS": count_ems, "Fire": count_fire, "Traffic": count_traffic}
    dictionary = [{"label": i , "value": j} for i,j in dictionary.items()]
    result = json.dumps(dictionary)
    return result

if __name__ == '__main__':
   app.run(debug = True)
