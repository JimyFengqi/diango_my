#coding:utf-8
import os  
import time  
import tushare as ts  
import pandas as pd  
import numpy as np
  
 
def my_data_input(): 
    data=[]
    for _ in range(6):  
        tmp={}
        tmp['code']=input('你的股票代码是：')
        tmp['origin_price']=input('你的股票买入价格是：')
        tmp['low_price']=input('期待的卖出价格：')
        tmp['High_price']=input('保底的价格：')
        data.append(tmp)
    return data


gu_code=['002070','002702','600202','600371','600462','601718','603899']
my_data=[{'高价': '4.10', 'code':'002070','低价': '4.51', '成本价': 4.475},        
         {'高价': '5.2', 'code':'002702','低价': '5.9', '成本价': 5.805},
         {'高价': '8.1', 'code': '600202', '低价': '8.9', '成本价': 8.825}, 
         {'高价': '10.1', 'code': '600371', '低价': '12.1', '成本价': 10.917},
         {'高价': '5.1', 'code': '600462', '低价': '6.1', '成本价': 5.910}, 
         {'高价': '5.0', 'code': '601718', '低价': '7.0', '成本价': 6.143},
         {'高价': '30.0', 'code': '603899', '低价': '26.0', '成本价': 29.451}]
        
def get_realtime_price(code_lists,my_data):
    #df2=pd.DataFrame(columns=['股票代码',"股票名字","当前价格","实时时间"])#创建一个空的数组格式
    df = ts.get_realtime_quotes(code_lists)
    #current_time = df[['time']]
    e=df.loc[:,['code','name','price']]
    e.rename(columns={'code':'股票代码','name':'股票名称','price':"当前价格"},inplace=True)
    origin_price = [value['成本价'] for value in my_data]
    low_price = [float(value['低价']) for value in my_data]
    high_price = [value['高价'] for value in my_data] 
    #current_price=e['当前价格']
    #print (current_price)
    new_current_price=e.iloc[:,2].values
    new_current_price=[float(item) for item in new_current_price]
    #print (origin_price)
    #print (new_current_price)
    #difference = [value, for i in range(len(origin_price)) value = origin_price[i]-new_current_price[i]]
    difference =list(map(lambda x:x[0]-x[1],zip(new_current_price,origin_price))) 
    rate=list(map(lambda x:x[0]/x[1]*100,zip(difference,origin_price)))
    
    #e['time'] = current_time
    print (difference)


    e['成本价'] =origin_price
    e['差价']  = difference
    
    #e['低价']  = low_price
    #e['高价']  =high_price
    e['盈利率']  =rate
    
    print (e)
    


        
get_realtime_price(gu_code,my_data)
        
