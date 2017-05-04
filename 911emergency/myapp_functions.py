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

def emergency_type():
    result = ['EMS', 'Fire', 'Traffic']
    return result

def type_trend_values(year,emergency_type):
    all_freq = data[data['timeStamp'].str.contains(year)]
    result = all_freq[all_freq['title'].str.contains(emergency_type)]
    result['title'] = result['title'].str.strip(emergency_type+ ":")
    result = result['title'].value_counts(ascending=True)[:]
    ems_top_5 = result.head(5)
    ems_bottom_5 = result.tail(5)
    result = ems_top_5.append(ems_bottom_5)
    y = result.index
    result_ret = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    count = 0
    while count < 10:
        result_ret[count] = y[count]
        count = count + 1
    return result_ret

#Emergency overview for an year input by the user
def emergency_overview(year):
    if (year == ''):
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

# print (emergency_overview(''))

#Trend for an Emergency sub-category in a specific year
def emergency_trend(year, emergency_type, sub_emergency_type):
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
    vehicle_accident = data[data['timeStamp'].str.contains('2016')]
    vehicle_accident = vehicle_accident[vehicle_accident['title'].str.contains('VEHICLE ACCIDENT')]
    result = [1]*12
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
def google_map():
    lat = data['lat']
    lng = data['lng']
    i = 0
    result = [1] * len(lat)
    while i < len(lat):
        l = []
        l.append(lat[i])
        l.append(lng[i])
        result[i] = l
        i = i + 1
    return result

#median household income data
def income_trend():
    income = {'2013': 76919, '2014' :79495, '2015': 83254 ,'2016' : 88275}
    return income

#Home value data
def home_value():
    cwd = os.getcwd() + '/' + 'home_values.csv'
    home_data = read_csv(cwd)
    home_d = home_data['Quarter']
    home_v = home_data['Values']
    home_value = dict(zip(home_d, home_v))
    for key in home_value:
        home_value[key] = int (home_value[key])
    home_value = [{"label": i, "value": j} for i, j in home_value.items()]
    return home_value

#small business data
def small_business():
    small_b = {'2013':{'Cleaning & Maintenance': 23889, 'material moving': 24343, 'Personal care': 13154, 'Food and serving': 11778},
               '2014':{'Cleaning & Maintenance': 23567, 'material moving': 22921, 'Personal care': 16632, 'Food and serving': 12931},
               '2015':{'Cleaning & Maintenance': 23422, 'material moving': 21601, 'Personal care': 17142,'Food and serving': 14167},
               '2016':{'Cleaning & Maintenance': 23011, 'material moving': 20222, 'Personal care': 18945,'Food and serving': 17498}}
    return small_b

#fake call expenditure
def emergency_expenditure():
    result = {'2015':[1029868,463005], '2016': [2035999,839475]}
    return result