from pandas import *
import datetime as dt
import json
import os

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
    return dictionary

#print (emergency_overview('2016'))

def emergency_trend(year, emergency_type, sub_emergency_type):
    trend_data = data[data['timeStamp'].str.contains(year)]
    x = trend_data[trend_data['title'].str.contains(emergency_type + " " + sub_emergency_type)]
    jan_count = len((x[x['timeStamp'].str.contains(year+'/1/')]).index)
    feb_count = len((x[x['timeStamp'].str.contains(year+'/2/')]).index)
    mar_count = len((x[x['timeStamp'].str.contains(year+'/3/')]).index)
    apr_count = len((x[x['timeStamp'].str.contains(year+'/4/')]).index)
    may_count = len((x[x['timeStamp'].str.contains(year+'/5/')]).index)
    jun_count = len((x[x['timeStamp'].str.contains(year+'/6/')]).index)
    jul_count = len((x[x['timeStamp'].str.contains(year+'/7/')]).index)
    aug_count = len((x[x['timeStamp'].str.contains(year+'/8/')]).index)
    sep_count = len((x[x['timeStamp'].str.contains(year+'/9/')]).index)
    oct_count = len((x[x['timeStamp'].str.contains(year+'/10/')]).index)
    nov_count = len((x[x['timeStamp'].str.contains(year+'/11/')]).index)
    dec_count = len((x[x['timeStamp'].str.contains(year+'/12/')]).index)
    dict_trend = {'Jan': jan_count, 'Feb': feb_count, 'Mar': mar_count, 'Apr': apr_count, 'May': may_count, 'Jun': jun_count, 'Jul': jul_count, 'Aug': aug_count, 'Sep': sep_count, 'Oct': oct_count, 'Nov': nov_count, 'Dec': dec_count}
    dict_trend = [{"label": i , "value": j} for i,j in dict_trend.items()]
    return dict_trend

#print (emergency_trend('2016', 'EMS:', 'ASSAULT VICTIM'))

def emergency_trend_comparison(year, emergency_type, sub_emergency_type1, sub_emergency_type2):
    trend_data = data[data['timeStamp'].str.contains(year)]
    trend1_data = trend_data[trend_data['title'].str.contains(emergency_type + " " + sub_emergency_type1)]
    jan_count = len((trend1_data[trend1_data['timeStamp'].str.contains(year+'/1/')]).index)
    feb_count = len((trend1_data[trend1_data['timeStamp'].str.contains(year+'/2/')]).index)
    mar_count = len((trend1_data[trend1_data['timeStamp'].str.contains(year+'/3/')]).index)
    apr_count = len((trend1_data[trend1_data['timeStamp'].str.contains(year+'/4/')]).index)
    may_count = len((trend1_data[trend1_data['timeStamp'].str.contains(year+'/5/')]).index)
    jun_count = len((trend1_data[trend1_data['timeStamp'].str.contains(year+'/6/')]).index)
    jul_count = len((trend1_data[trend1_data['timeStamp'].str.contains(year+'/7/')]).index)
    aug_count = len((trend1_data[trend1_data['timeStamp'].str.contains(year+'/8/')]).index)
    sep_count = len((trend1_data[trend1_data['timeStamp'].str.contains(year+'/9/')]).index)
    oct_count = len((trend1_data[trend1_data['timeStamp'].str.contains(year+'/10/')]).index)
    nov_count = len((trend1_data[trend1_data['timeStamp'].str.contains(year+'/11/')]).index)
    dec_count = len((trend1_data[trend1_data['timeStamp'].str.contains(year+'/12/')]).index)
    dict_trend1 = {'Jan': jan_count, 'Feb': feb_count, 'Mar': mar_count, 'Apr': apr_count, 'May': may_count, 'Jun': jun_count, 'Jul': jul_count, 'Aug': aug_count, 'Sep': sep_count, 'Oct': oct_count, 'Nov': nov_count, 'Dec': dec_count}
    dict_trend1 = [{"label": i , "value": j} for i,j in dict_trend1.items()]
    trend2_data = trend_data[trend_data['title'].str.contains(emergency_type + " " + sub_emergency_type2)]
    jan_count = len((trend2_data[trend2_data['timeStamp'].str.contains(year+'/1/')]).index)
    feb_count = len((trend2_data[trend2_data['timeStamp'].str.contains(year+'/2/')]).index)
    mar_count = len((trend2_data[trend2_data['timeStamp'].str.contains(year+'/3/')]).index)
    apr_count = len((trend2_data[trend2_data['timeStamp'].str.contains(year+'/4/')]).index)
    may_count = len((trend2_data[trend2_data['timeStamp'].str.contains(year+'/5/')]).index)
    jun_count = len((trend2_data[trend2_data['timeStamp'].str.contains(year+'/6/')]).index)
    jul_count = len((trend2_data[trend2_data['timeStamp'].str.contains(year+'/7/')]).index)
    aug_count = len((trend2_data[trend2_data['timeStamp'].str.contains(year+'/8/')]).index)
    sep_count = len((trend2_data[trend2_data['timeStamp'].str.contains(year+'/9/')]).index)
    oct_count = len((trend2_data[trend2_data['timeStamp'].str.contains(year+'/10/')]).index)
    nov_count = len((trend2_data[trend2_data['timeStamp'].str.contains(year+'/11/')]).index)
    dec_count = len((trend2_data[trend2_data['timeStamp'].str.contains(year+'/12/')]).index)
    dict_trend2 = {'Jan': jan_count, 'Feb': feb_count, 'Mar': mar_count, 'Apr': apr_count, 'May': may_count, 'Jun': jun_count, 'Jul': jul_count, 'Aug': aug_count, 'Sep': sep_count, 'Oct': oct_count, 'Nov': nov_count, 'Dec': dec_count}
    dict_trend2 = [{"label": i , "value": j} for i,j in dict_trend2.items()]
    dict_trend = {'trend1': dict_trend1 , 'trend2': dict_trend2}
    dict_trend = [{"label": i , "value": j} for i,j in dict_trend.items()]
    return dict_trend

#print (emergency_trend_comparison('2016', 'EMS:', 'ASSAULT VICTIM', 'CARDIAC EMERGENCY'))