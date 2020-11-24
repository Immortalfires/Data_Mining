# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 08:13:14 2020

@author: DELL
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

def load_file(path):
    raw_data = pd.read_csv(path,header=None)
    #原始数据
    raw_matrix = raw_data.values
    #取前两列分析
    data=raw_matrix[:,0:2]
    return data

def distance(data,centers):
    res = np.zeros((data.shape[0],centers.shape[0]))
    for i in range(len(data)):
        for j in range(len(centers)):
            res[i][j]=np.sqrt(np.sum((centers[j]-data[i])**2))
    return res

def near_center(data,centers):
    dist = distance(data,centers)
    near_cen=np.argmin(dist,1)
    return near_cen
   
def k_means(data,k):
    #随机初始化簇中心

    result = random.sample(range(0,len(data)),k)
    centers = np.zeros((k,2))
    for i in range(k):
        centers[i] = data[result[i]]
    print('原始簇中心：',result)
    
    #centers=np.random.choice(np.arange(0.4,0.8,0.05),(k,2),replace=False)
    for _ in range(20):
        #计算点归属
        near_cen = near_center(data,centers)
        #簇中心的更新
        for i in range(k):
            centers[i] = data[near_cen==i].mean()
        print('第',_,'次：',centers)
    return centers,near_cen

    
if __name__=="__main__":
    data=load_file('melon.csv')
    #2簇
    centers,near_cen = k_means(data,2)
    
    #print("结果簇中心：",centers)
    print("点的归属簇：",near_cen)
    plt.figure()
    plt.xlabel('destiny')
    plt.ylabel('sugercontent') 
    plt.scatter(data[:,0],data[:,1],c=near_cen)
    print(centers)
    plt.scatter(centers[:,0],centers[:,1],marker='v',s=250,c='r')
    plt.show()