from pandas import *
from pylab import *
import datetime as dt
from matplotlib import pyplot as plt
import numpy as np
from dateutil.parser import parse
from matplotlib import style

# read 911 csv
data = read_csv("/Users/manika/Documents/SJSU/CMPE272/project/montgomeryPA_911.csv")
pandas.to_datetime(data['timeStamp'])


# seperating different emergency data for every year and plotting it
def read_emergency_data(year, emergency_type):
    emergency_data = data[data['title'].str.contains(emergency_type)]
    emergency_data = emergency_data[emergency_data['timeStamp'].str.contains(year)]
    emergency_data = emergency_data.ix[0:, ['title']]
    emergency_data['title'] = emergency_data['title'].map(lambda x: x.lstrip(emergency_type).rstrip('aAbBcC'))
    emergency_frequency = emergency_data['title'].value_counts(ascending=True)[:]
    ax = emergency_frequency.plot(kind='barh', figsize=(15, 20))
    ax.set_xlabel("frequency")
    ax.set_ylabel(emergency_type + '_' + "type")
    return plt.show()


def emergency_overview(year):
    overview_data = data[data['timeStamp'].str.contains(year)]
    overview_data_ems = overview_data[overview_data['title'].str.contains('EMS:')]
    overview_data_fire = overview_data[overview_data['title'].str.contains('Fire:')]
    overview_data_traffic = overview_data[overview_data['title'].str.contains('Traffic:')]
    count_ems = len(overview_data_ems.index)
    count_fire = len(overview_data_fire.index)
    count_traffic = len(overview_data_traffic.index)
    dictionary = {"EMS": count_ems, "Fire": count_fire, "Traffic": count_traffic}
    plt.bar(range(len(dictionary)), dictionary.values(), align='center')
    plt.xticks(range(len(dictionary)), list(dictionary.keys()))
    plt.ylabel('Frequency')
    plt.xlabel('Emergency_type')
    plt.title('Emergency Overview in the year ' + year, fontsize=18)
    return plt.show()


e_data = data[data['timeStamp'].str.contains('2016')]
e_data = e_data[e_data['title'].str.contains('EMS:')]
e_data_freq = e_data['title'].value_counts()[:]
e_data_f = e_data_freq.to_frame(name=None)
# e_data_freq.ix[0:, :15]
e_data_f = e_data_f.rename(columns={'title': 'counts'})
e_data_f1 = e_data_f[e_data_f['counts'] > 800]
e_data_f2 = e_data_f[e_data_f['counts'] < 11]


# print (e_data_f2)

def emergency_trend(year, emergency_type, sub_emergency_type):
    trend_data = data[data['timeStamp'].str.contains(year)]
    trend_data = trend_data[trend_data['title'].str.contains(emergency_type + " " + sub_emergency_type)]
    return trend_data


x = emergency_trend('2016', 'EMS:', 'ASSAULT VICTIM')

e_data = data[data['timeStamp'].str.contains('2015')]
e_data = e_data[e_data['title'].str.contains('EMS:')]

#for item in e_data['timeStamp']:
    # item = DatetimeIndex(item).month
 #   print(item.month)

# e_data['timeStamp'] = DatetimeIndex(e_data['timeStamp']).month
# e_data['timeStamp'] = DateTimeIndex(e_data['timeStamp']).month
# e_freq = e_data1['Month'].value_counts()[ : ]
# e_data_freq = e_data['timeStamp'].value_counts(ascending = True)[ : ]
# print (e_data_freq)
# print (e_data['timeStamp'])
# e_data.sort_values(by='timeStamp')
# e_data.index = e_data['timeStamp']
# e_data['timeStamp'] = DatetimeIndex(e_data['timeStamp']).month

# GB=e_data.groupby([(e_data.index.month)]).sum()
# g = e_data.groupby(pandas.TimeGrouper("M"))
# print (e_data['timeStamp'])
# e_data = e_data['timeStamp'].value_counts()[ : ]



