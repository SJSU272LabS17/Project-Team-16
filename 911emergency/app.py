from flask import Flask, render_template, request, make_response, flash, redirect, session, abort, jsonify
import json
from urllib.request import urlopen
from functions import *

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

#print (heat_map('2016'))
#print(emergency_trend_comparison('2016', 'EMS:', 'ASSAULT VICTIM', 'CARDIAC EMERGENCY'))
#print (emergency_trend('2016', 'EMS:', 'ASSAULT VICTIM'))
#print (emergency_overview('2016'))

if __name__ == '__main__':
    app.run(debug = True)
