import itertools
from flask import Flask, render_template, request, make_response, flash, redirect, session, abort, jsonify
from pandas import *
import datetime as dt
import json
import os
import numpy as np
from itertools import groupby
import myexception

# read 911 csv
cwd = os.getcwd() + '/' + 'montgomeryPA_911.csv'
data = read_csv(cwd)

# converting the timestamp to pandas datetime format
pandas.to_datetime(data['timeStamp'])

#Generate emergency types
def category():
    result = ['EMS', 'Fire', 'Traffic']
    return result

#Generate sub-emergency types
def sub_category(year,emergency_type):
    all_freq = data[data['timeStamp'].str.contains(year)]
    result = all_freq[all_freq['title'].str.contains(emergency_type)]
    df = pandas.DataFrame(result['title'])
    l = [1] * len(result['title'])
    i = 0;
    df_new = df.values.tolist()
    while i < len(df_new):
        l[i] = df_new[i][0][5:]
        i = i + 1
    from collections import defaultdict
    fq = defaultdict(int)
    for w in l:
        fq[w] += 1
    dict1 = {}
    a1_sorted_keys = sorted(fq, key=fq.get, reverse=True)
    for r in a1_sorted_keys:
        dict1[r] = fq[r]
    len1 = len(dict1)
    result = []
    result = list(dict1)[:5] + list(dict1)[len1-5:len1]
    return result

#Emergency overview for an year input by the user
def emergency_overview(year):
    if year == '':
         raise myexception.CheckPostData("Year is empty")
    overview_data = data[data['timeStamp'].str.contains(year)]
    overview_data_ems = overview_data[overview_data['title'].str.contains('EMS:')]
    overview_data_fire = overview_data[overview_data['title'].str.contains('Fire:')]
    overview_data_traffic = overview_data[overview_data['title'].str.contains('Traffic:')]
    count_ems = len(overview_data_ems.index)
    count_fire = len(overview_data_fire.index)
    count_traffic = len(overview_data_traffic.index)
    dictionary = {"EMS": count_ems, "Fire": count_fire, "Traffic": count_traffic}
    dictionary = [{"label": i , "value": j} for i,j in dictionary.items()]
    return dictionary

#Trend for an Emergency sub-category in a specific year
def emergency_trend(year, emergency_type, sub_emergency_type):
    if year == '':
        raise myexception.CheckPostData("Year is empty")
    elif emergency_type == '':
        raise myexception.CheckPostData("Emergency Type is empty")
    elif sub_emergency_type == '':
        raise myexception.CheckPostData("Sub-Emergency Type is empty")

    trend_data = data[data['timeStamp'].str.contains(year)]
    trend_data = trend_data[trend_data['title'].str.contains(sub_emergency_type)]
    month = ['1454195838', '1456874238', '1459379838', '1462058238', '1464650238',
             '1467328638', '1469920638', '1472599038', '1475277438', '1477869438',
             '1480547838', '1483139838']
    dict_trend = {}
    for i in range(1, 13):
        count = len((trend_data[trend_data['timeStamp'].str.contains(year+'/'+str(i)+'/')]).index)
        dict_trend[month[i-1]] = count
    trend_data_arr = []
    for key in dict_trend:
        l = []
        l.append(int(key))
        l.append(dict_trend[key])
        trend_data_arr.append(l)
    return trend_data_arr

#Trend comparison for two sub-categories of an emergency type for a specific year
def emergency_trend_comparison(year, emergency_type, sub_emergency_type1, sub_emergency_type2):
    dict_trend1 = emergency_trend(year, emergency_type, sub_emergency_type1)
    dict_trend2 = emergency_trend(year, emergency_type, sub_emergency_type2)
    dict_trend = {sub_emergency_type1: dict_trend1 , sub_emergency_type2: dict_trend2}
    dict_trend = [{"label": i , "value": j} for i,j in dict_trend.items()]
    return dict_trend

#Hourly data for plotting Heap map for Vehicle accidents
def heat_map(year):
    vehicle_accident = data[data['timeStamp'].str.contains(year)]
    vehicle_accident = vehicle_accident[vehicle_accident['title'].str.contains('VEHICLE ACCIDENT')]
    result = [1] * 12
    for i in range(1, 13):
        l = []
        for j in range(0, 24):
            accidents_month = vehicle_accident[vehicle_accident['timeStamp'].str.contains('/' + str(i) + '/')]
            accidents_month = accidents_month[accidents_month['timeStamp'].str.contains(' ' + str(j) + ':')]
            count = len(accidents_month)
            l.append(count)
        result[i - 1] = l
    return result

#google map latitude longitude data
def google_map(year):
    overview_data = data[data['timeStamp'].str.contains(year)]
    # print (len (overview_data))
    title = data['title']
    lat = data['lat']
    lng = data['lng']
    i = 0
    result = []
    j = 0
    while i < len(lat):
        if year in data['timeStamp'][i]:
            j = j + 1
            l = []
            l.append(lat[i])
            l.append(lng[i])
            if "EMS" in title[i]:
                l.append("EMS")
            elif "Fire" in title[i]:
                l.append("Fire")
            elif "Traffic" in title[i]:
                l.append("Traffic")
            result.append(l)
        i = i + 1
    return result

#median household income data
def income_trend():
    income = {'2013': 76919, '2014' :79495, '2015': 83254 ,'2016' : 88275}
    return income

#Home value data
def home_value():
    count_2013 = 8850159
    count_2014 = 8244159
    overview_data_2015 = data[data['timeStamp'].str.contains('2015')]
    count_2015 = len(overview_data_2015.index)
    overview_data_2016 = data[data['timeStamp'].str.contains('2016')]
    count_2016 = len(overview_data_2016.index)
    overview_data_2017 = data[data['timeStamp'].str.contains('2017')]
    count_2017 = len(overview_data_2017.index)
    cwd = os.getcwd() + '/' + 'home_values.csv'
    home_data = read_csv(cwd)
    home_d = home_data['Year']
    home_v = home_data['Value']
    result = [{"label": "911 calls", "value" : [[int(home_d[0]),count_2013],[int(home_d[1]),count_2014],[int(home_d[2]),count_2015],[int(home_d[3]),count_2016],[int(home_d[4]),count_2017]]},
               {"label" : "Home Value", "value" : [[int(home_d[0]),int(home_v[0])],[int(home_d[1]),int(home_v[1])],[int(home_d[2]),int(home_v[2])],[int(home_d[3]),int(home_v[3])],[int(home_d[4]),int(home_v[4])]]}]
    return result

#small business data
def small_business():
    count_2013 = 8850159
    count_2014 = 8244159
    overview_data_2015 = data[data['timeStamp'].str.contains('2015')]
    count_2015 = len(overview_data_2015.index)
    overview_data_2016 = data[data['timeStamp'].str.contains('2016')]
    count_2016 = len(overview_data_2016.index)
    small_b = [{"label" : "Cleaning & Maintenance", "value": [[2013, 23889], [2014, 23567], [2015, 23422], [2016, 23011]]}, \
               {"label" : "material moving", "value": [[2013, 24343], [2014, 22921], [2015, 21601], [2016, 20222]]}, \
               {"label" : "Personal care", "value": [[2013, 13154], [2014, 16632], [2015, 17142], [2016, 18945]]}, \
               {"label" : "Food and serving", "value": [[2013, 11778], [2014, 12931], [2015, 14167], [2016, 17498]]},
               {"label": "911 calls", "value": [[2013, count_2013], [2014, count_2014], [2015, count_2015], [2016, count_2016]]}]
    return small_b

#fake call expenditure
def emergency_expenditure():
    result = {'2015':[1029868,463005], '2016': [2035999,839475]}
    return result


