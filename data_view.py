# coding=utf8
import pandas as pd
import matplotlib.pyplot as plt
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

shop_id = 1

data = pd.read_csv('input/%d.csv'%shop_id , encoding='utf-8')
data = data[['result']]
data.plot(kind='line')
plt.show()

