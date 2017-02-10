# coding=utf8

import pandas as pd
import numpy as np

result = {}
years = [2015,2016]
months = [31,28,31,30,31,30,31,31,30,31,30,31]

cur = 3

for year in years:
    for month in range(1 , 13):
        max_day = months[month - 1]
        if(month == 2 and year == 2016):
            max_day = 29
        for day in range(1 , max_day + 1):
            str_month = str(month)
            if(month < 10):
                str_month = '0' + str(month)
            str_day = str(day)
            if(day < 10):
                str_day = '0' + str(day)
            result['%s-'%year+str_month+'-'+str_day] = [cur]
            cur = (cur + 1) % 7

print result
