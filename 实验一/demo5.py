# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 16:54:28 2020

@author: DELL
"""
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn import decomposition
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

#读入文件并加上表头
data = pd.read_csv('iris.csv',header=None,names=['SepalLength','SepalWidth','PetalLength','PetalWidth','Species']);


sns.boxplot(x='Species', y='PetalLength', data=data)
#sns.FacetGrid(data, hue="Species", size=5) \
#    .map(plt.scatter, "SepalLength", "SepalWidth") \
#    .add_legend();

#sns.pairplot(data, hue='Species', size=3, diag_kind='kde')

#归一化处理
martix=data[['SepalLength','SepalWidth','PetalLength','PetalWidth']]
print('归一化处理')
minVals = martix.min(0);
maxVals = martix.max(0)
ranges = maxVals - minVals;
normData = np.zeros(np.shape(data));
m = martix.shape[0];
normData = martix - np.tile(minVals, (m, 1));
normData = normData/np.tile(ranges, (m, 1));
print(normData);


#PCA处理
pca = PCA(n_components=2,whiten='true')   #降到2维
pca.fit(martix)                  #训练
newX=pca.fit_transform(martix)   #降维后的数据
print('PCA处理')
print(pca.explained_variance_ratio_)  #输出贡献率
print(newX)                  #输出降维后的数据

iris = load_iris()
y_data = iris.target

plt.figure()
x=np.array(newX)[:,0];
y=np.array(newX)[:,1];
plt.scatter(x,y,c=y_data);
plt.show()