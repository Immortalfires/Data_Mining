# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 16:32:03 2020

@author: DELL
"""
import pandas as pd
import numpy as np

data1 = pd.read_csv('ReaderInformation.csv');
data2 = pd.read_csv('ReaderRentRecode.csv');

#观察数据
print(data1.info())
print(data2.info())

data3 = pd.merge(data1,data2,on='num')
data3.to_csv('combineData.csv',encoding='utf-8')