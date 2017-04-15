from flask import Flask, render_template, request, make_response, flash, redirect, session, abort
from pandas import *
from pylab import *
import datetime as dt
from matplotlib import pyplot as plt
import numpy as np
from dateutil.parser import parse
from matplotlib import style
import random
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.dates import DateFormatter
import io
from io import StringIO
import base64
import json
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from urllib.request import urlopen

app = Flask(__name__)

@app.route('/')

def index():
   return render_template('index.html')

@app.route('/emergency', methods=['GET', 'POST'])

def emergency():
    if request.method == 'POST':
        year = request.form.get('year_select')
        result = json.loads(emergency_overview(year))

    return render_template('emergency.html', result=result, year=year)


# read 911 csv
data = read_csv("/Users/manika/Documents/SJSU/CMPE272/project/montgomeryPA_911.csv")
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
    #y = emergency_overview('2016')
    result = json.dumps(dictionary)
    #loaded_z = json.loads(z)
    #plt.bar(range(len(dictionary)), dictionary.values(), align='center')
    #plt.xticks(range(len(dictionary)), list(dictionary.keys()))
    #plt.ylabel('Frequency')
    #plt.xlabel('Emergency_type')
    #plt.title('Emergency Overview in the year ' + year, fontsize=18)
    return result




if __name__ == '__main__':
   app.run(debug = True)

