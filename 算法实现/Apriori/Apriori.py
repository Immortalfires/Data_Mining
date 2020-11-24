# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 19:09:16 2020

@author: Au revoir

Aprior算法实现
1. 若一个项集为频繁项集，则其所有非空子集也是频繁项集
2. 若一个非空项集为非频繁项集，则其所有父集也是非频繁项集

设置最小支持度为2
ck：候选项集
lk：频繁项集
"""
import itertools

#加载文件
def load_Data(path):
    data=[]
    with open(path,encoding="UTF-8") as f:
        for line in f:
            line = line.strip("\n");
            data.append(line.split(","));
    return data

#生成候选一项集
def buildC1(dataset):
    #弄成一维数组并放入set去重,放入不可变集合
    item1=set(itertools.chain(*dataset))
    return [frozenset([i]) for i in item1]

#基于候选一项集生成频繁一项集
def ck_to_lk(dataset,ck,min_support):
    support={}
    for row in dataset:
        for item in ck:
            if item.issubset(row):
                support[item] = support.get(item,0)+1
    total = len(dataset)
    return {k:v/total for k,v in support.items() if v/total >= min_support}

#频繁k项集生成候选k+1项集
def lk_to_ck(lk_list):
    ck=set()
    lk_size=len(lk_list)
    if lk_size>1:
        k=len(lk_list[0])
        for i,j in itertools.combinations(range(lk_size),2):
            t=lk_list[i]|lk_list[j]
            if(len(t)==k+1):
                ck.add(t)
    return ck

#生成所有频繁项集
def get_L_all(dataset,min_support):
    c1=buildC1(dataset)
    print('候选一项集：',c1,'\n')
    L1=ck_to_lk(dataset,c1,min_support)
    print('频繁一项集：',L1,'\n')
    L_all=L1
    Lk=L1
    while(len(Lk)>1):
        lk_key_list=list(Lk.keys())
        ck=lk_to_ck(lk_key_list)
        Lk=ck_to_lk(dataset,ck,min_support)
        if(len(Lk)>0):
            L_all.update(Lk)
            print('生成所有的频繁项集',Lk,"\n")
        else:
            break
    return L_all

#生成关联规则
def rules_from_item(item):
    left=[]
    for i in range(1,len(item)):
        #得到左边部分
        left.extend(itertools.combinations(item,i))
    #求差集得到右边部分
    return [(frozenset(le),frozenset(item.difference(le))) for le in left]

#从所有频繁项集字典中，生成关联规则列表
def rules_from_L_all(L_all,min_confidence):
    print('从所有频繁项集字典中，生成关联规则')
    rules=[]
    for Lk in L_all:
        if(len(Lk)>1):
            rules.extend(rules_from_item(Lk))
           # print('生成关联规则：',rules_from_item(Lk),"\n")
    res=[]
    for left,right in rules:
        support=L_all[left|right]
        confidence=support/L_all[left]
        if(confidence>=min_confidence):
            final = [left|right]
            print({"左侧":left,"整体":final,"支持度":support,"置信度":confidence},'\n')
            res.append({"左侧":left,"整体":final,"支持度":support,"置信度":confidence})
    return res


if __name__=="__main__":
    #最小支持度
    min_support=0.3
    #最小置信度
    min_confidence=0.7
    #读入数据
    dataset=load_Data("data.txt")
    for i in range(5):
        print(i+1,dataset[i],sep="->")
    #为了减少开销，将字符串映射成数字
    #拆包，转为一维
    items=set(itertools.chain(*dataset))
    str_to_index={}
    index_to_str={} 
    print(items)
    for index,item in enumerate(items):
        str_to_index[item]=index
        index_to_str[index]=item
    print("字符串到编号",list(str_to_index.items())[:len(items)])
    print("编号到字符串",list(index_to_str.items())[:len(items)],'\n')
    """
    for i in range(len(dataset)):
        for j in range(len(dataset[i])):
            dataset[i][j] = str_to_index[dataset[i][j]]
    
    for i in range(5):
        print(i+1,dataset[i],sep="->")
    
    c1=buildC1(dataset)
    print(c1,'\n')
    L1=ck_to_lk(dataset,c1,min_support)
    print(L1,'\n')
    c2=lk_to_ck(list(L1.keys()))
    print(c2,'\n')
    L2=ck_to_lk(dataset,c2,min_support)
    print(L2,'\n')
    """
    L_all=get_L_all(dataset,min_support)
    res=rules_from_L_all(L_all,min_confidence)
    #print(res)