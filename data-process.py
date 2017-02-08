# coding=utf8
import pandas as pd
import matplotlib.pyplot as plt
import json
import numpy as np
import math
import xgboost as xgb
from scipy import sparse
from sklearn.feature_extraction import FeatureHasher
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, scale
from sklearn.decomposition import TruncatedSVD, SparsePCA
from sklearn.cross_validation import train_test_split, cross_val_score
from sklearn.feature_selection import SelectPercentile, f_classif, chi2
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.metrics import log_loss
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import SelectFromModel
from sklearn.preprocessing import OneHotEncoder
from sklearn.feature_extraction import DictVectorizer

from datetime import datetime
from datetime import timedelta

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras import backend as K
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error

plt.style.use('ggplot')

work_path = '../..'

def plot_user_pay(user_pay , shop_id):
	tmp = user_pay[user_pay['shop_id'] == shop_id]
	tmp.drop_duplicates(['shop_id','date'], keep='first', inplace=True)
	tmp = tmp.sort_values('date')
	tmp.plot(x = 'date' , y = ['result','user_count'] , kind='line')
	plt.show()


def generate_user_pay(user_pay , shop_id , time_index):
	data = user_pay[user_pay['shop_id'] == shop_id]
	data = data[['date', 'result' , 'name']]
	data.drop_duplicates(['date'], keep='first', inplace=True)
	data = data.sort_values('date')
	# data = pd.merge(time_index, data, on='date', how='outer')
	# data = data.fillna(0)
	# data = data[['result']]
	# data.index = pd.Index(time_index)
	return data


print("# Read city_info")
f = open('locality-2.txt', 'r')
lines = f.readlines()
localities = []
for line in lines:
	tmp = line.split(',')
	localities.append([tmp[0] , tmp[1].replace("\n","")])
print localities

city_info = pd.DataFrame(localities)
city_info.columns = ['city_name','name']

print len(city_info)
print city_info.head(5)


print("# Read aqi_info")

f = open('aqi.jl', 'r')
lines = f.readlines()
aqi_result = {}
for locality in localities:
	data = []
	for line in lines:
		jo = json.loads(line)
		city_name = jo['item_id'].split('_')[0]
		if(city_name == locality[1]):
			data.append([jo['weather_quality'],jo['weather_So3'],
						 jo['weather_O3'] , jo['weather_pm25'] ,
						 jo['weather_pm10'] , jo['weather_No2'] , jo['weather_aqi'] , jo['weather_Co'],jo['item_id'].split('_')[1]])
	print locality[1]
	if(locality[1] == 'tianmen'):
		continue
	tmp = pd.DataFrame(data)
	tmp.columns = ['weather_quality' , 'weather_So3' , 'weather_O3'  , 'weather_pm25'
			, 'weather_pm10' , 'weather_No2' , 'weather_aqi' , 'weather_Co' , 'date']
	aqi_result[locality[1]] = tmp

print("# Read shop_info")

shop_info = pd.read_csv("%s/dataset/shop_info.txt"%work_path, header=None)
shop_info.columns = ['shop_id', 'city_name', 'location_id', 'per_pay', 'score', 'comment_cnt', 'shop_level', 'cate_1_name', 'cate_2_name', 'cate_3_name']
shop_info = shop_info.fillna(0)

shop_info = shop_info[['shop_id' , 'city_name']]

shop_info = pd.merge(shop_info , city_info , left_on='city_name')

print shop_info.head(5)

print("# Read user_pay")
user_pay = pd.read_csv("%s/dataset/user_pay.txt"%work_path, header=None)

print("# add user_pay columns")
user_pay.columns = ['user_id', 'shop_id', 'time_stamp']

print("# fill NaN")
user_pay = user_pay.fillna(0)

print("# Cal per_day result")
user_pay['date'] = user_pay['time_stamp'].apply(lambda x: x.split(' ')[0])
user_pay['result'] = user_pay.groupby(['shop_id','date'])['time_stamp'].transform('count')

print("# Cal per_day user count")
user_pay.drop_duplicates(['user_id','shop_id','date'], keep='first', inplace=True)
user_pay['user_count'] = user_pay.groupby(['shop_id', 'date'])['user_id'].transform('count')

user_pay = user_pay[['user_id', 'shop_id' , 'date' , 'result' , 'user_count']]

time_index = user_pay[['date']]
time_index.drop_duplicates('date', keep='first', inplace=True)
time_index = time_index.sort_values('date')

user_pay = pd.merge(user_pay , shop_info , left_on='shop_id')

print user_pay.head(5)
print user_pay.tail(5)

shop_id = 1

data = generate_user_pay(user_pay , shop_id , time_index)

print len(data)
print data.head(5)
print data.tail(5)

data = pd.merge(data , aqi_result[shop_info[shop_info['shop_id'] == shop_id]['name']] , left_on='date')

# for shop_id in range(1 , 10):
# 	data = generate_user_pay(user_pay, shop_id, time_index)
# 	data.to_csv('%d.csv'%shop_id , encoding = 'utf-8' , index = False)

data.to_csv('%d.csv'%shop_id , encoding = 'utf-8' , index = False)
print 'complete'



