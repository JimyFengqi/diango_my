#coding:utf-8
import os  
import time  
import tushare as ts  
import pandas as pd  
  
 
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
    print ('2222')
    #current_time = df[['time']]
    e=df.loc[:,['code','name','price']]
    e.rename(columns={'code':'股票代码','name':'股票名称','price':"当前价格"},inplace=True)
    e['成本价']  = [value['成本价'] for value in my_data]
    e['低价']  = [float(value['低价']) for value in my_data]
    e['高价']  = [value['高价'] for value in my_data]    
  
    #e['time'] = current_time
    
  
    print (e)


        
get_realtime_price(gu_code,my_data)
        
