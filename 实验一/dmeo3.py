# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np
#读入文件
data = pd.read_csv('movie_metadata.csv');
"""
#原始数据形状
print(data.shape)

#查看数据前5行

"""
print(data.head(5))
#查看基本统计信息
print(data.info())
print(data.isnull().sum());
#删除重复值
data.drop_duplicates()
#至少有2个空值才能删除行
data.dropna(thresh=2)
#为country添加默认值为空
data.country= data.country.fillna('');
#为num_critic_for_reviews添加默认值为0
data.num_critic_for_reviews = data.num_critic_for_reviews.fillna(0)
#为director_facebook_likes添加默认值为0
data.director_facebook_likes = data.director_facebook_likes.fillna(0)
#为actor_3_facebook_likes添加默认值为0
data.actor_3_facebook_likes = data.actor_3_facebook_likes.fillna(0)
#为actor_1_facebook_likes添加默认值为0
data.actor_1_facebook_likes = data.actor_1_facebook_likes.fillna(0)
#为facenumber_in_poster添加默认值为0
data.facenumber_in_poster = data.facenumber_in_poster.fillna(0)
#为budget添加默认值为0
data.budget = data.budget.fillna(0)
#为actor_2_name添加默认值为anonymous 
data.actor_2_name = data.actor_2_name.fillna('anonymous')
#为actor_1_name添加默认值为anonymous 
data.actor_1_name = data.actor_1_name.fillna('anonymous')
#为actor_3_name添加默认值为anonymous 
data.actor_3_name = data.actor_3_name.fillna('anonymous')
#为duration添加默认值为平均值
data.duration = data.duration.fillna(data.duration.mean());
#为color添加默认值为空
data.color = data.color.fillna('');
#为gross添加默认值为0
data.gross = data.gross.fillna(0);
#去除不知道上映年份的电影
data.dropna(subset=['title_year']);
#该字段内容大写并去除末尾空格
data['movie_title'].str.upper();
data['movie_title'].str.strip();
data.to_csv('movie_metadata_cleanfile.csv',encoding='utf-8')