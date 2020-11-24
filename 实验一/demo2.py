# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 08:35:48 2020

@author: DELL
"""
import pandas as pd
import matplotlib.pyplot as plt

f = open('西安北京年薪数据.csv')
data = pd.read_csv(f,encoding='utf-8')

xian = data['西安'];
beijing = data['北京'];
 #计算北京和西安均值、方差、标准差
print('西安年薪均值：{}，方差：{}，标准差：{}'.format(xian.mean(),xian.var(),xian.std()));
print('北京年薪均值：{}，方差：{}，标准差：{}'.format(beijing.mean(),beijing.var(),beijing.std()));
#箱体图
plt.figure();
plt.boxplot((xian,beijing),labels=('xian','beijing'))
plt.show();
#小提琴图
plt.figure();
plt.violinplot(dataset=(xian,beijing),showmeans=True,showmedians=True)
plt.show()
