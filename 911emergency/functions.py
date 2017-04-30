from flask import Flask, render_template, request, make_response, flash, redirect, session, abort, jsonify
from pandas import *
import datetime as dt
import json
import os
import numpy as np

# read 911 csv
cwd = os.getcwd() + '/' + 'montgomeryPA_911.csv'
data = read_csv(cwd)

# converting the timestamp to pandas datetime format
pandas.to_datetime(data['timeStamp'])

#Emergency overview for an year input by the user
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
    return dictionary

#print (emergency_overview('2016'))

#Trend for an Emergency sub-category in a specific year
def emergency_trend(year, emergency_type, sub_emergency_type):
    trend_data = data[data['timeStamp'].str.contains(year)]
    trend_data = trend_data[trend_data['title'].str.contains(emergency_type + ": " + sub_emergency_type)]
    month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    dict_trend = {}
    for i in range(1, 13):
        count = len((trend_data[trend_data['timeStamp'].str.contains(year+'/'+str(i)+'/')]).index)
        dict_trend[month[i-1]] = count
        trend_data_dict = [{"label": i , "value": j} for i,j in dict_trend.items()]
    return trend_data_dict

#print (emergency_trend('2016', 'EMS:', 'ASSAULT VICTIM'))

#Trend comparison for two sub-categories of an emergency type for a specific year
def emergency_trend_comparison(year, emergency_type, sub_emergency_type1, sub_emergency_type2):
    dict_trend1 = emergency_trend(year, emergency_type, sub_emergency_type1)
    dict_trend2 = emergency_trend(year, emergency_type, sub_emergency_type2)
    dict_trend = {sub_emergency_type1: dict_trend1 , sub_emergency_type2: dict_trend2}
    dict_trend = [{"label": i , "value": j} for i,j in dict_trend.items()]
    return dict_trend

#print (emergency_trend_comparison('2016', 'EMS:', 'ASSAULT VICTIM', 'CARDIAC EMERGENCY'))

#Hourly data for plotting Heap map for Vehicle accidents
def heat_map(year):
    month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    vehicle_accident = data[data['timeStamp'].str.contains(year)]
    vehicle_accident = vehicle_accident[vehicle_accident['title'].str.contains('VEHICLE ACCIDENT')]
    dict_monthly = {}
    dict_hourly = {}
    for i in range(1, 13):
        for j in range(0, 24):
            accidents_month = vehicle_accident[vehicle_accident['timeStamp'].str.contains('/i/')]
            count = len((vehicle_accident[vehicle_accident['timeStamp'].str.contains(' ' + str(j) + ':')]).index)
            dict_hourly[str(j)+':00'] = count
        dict_hourly_new = [{"label": i , "value": j} for i,j in dict_hourly.items()]
        dict_monthly[month[i-1]] = dict_hourly_new
        dict_monthly_hourly = [{"label": i , "value": j} for i,j in dict_monthly.items()]
    return dict_monthly_hourly

# print (heat_map('2016'))

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

#google map data

def google_map():
    map_lat = data['lat']
    map_lng = data['lng']
    google_map = dict(zip(map_lat, map_lng))
    for key in google_map:
        google_map[key] = float(google_map[key])
        key = str(key)
    return google_map
    #return google_map

#print (google_map())

