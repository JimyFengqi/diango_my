# -*- coding: utf-8 -*-


'''
运行本程序,需要
python3,linux环境
1.安装selenium,
2.谷歌浏览器,跟谷歌浏览器配套的chromedriver
3.geckodriver
4.安装tushare, pandas模块

'''
import tushare as ts
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
#导入本地IP池
from ips import _get_ip

#虚拟浏览器,没有实体
def simulator_driver():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    #chrome_options.add_argument('--proxy-server=http://%s' % _get_ip()) #这里可以设置代理
    driver = webdriver.Chrome(chrome_options=chrome_options)
    return driver
#模拟手机浏览器,这里模拟的是安卓4.2.1    
def mobile_driver():
    mobile_emulation = {"deviceMetrics": {"width": 750, "height": 1334, "pixelRatio": 6.0}, # 定义设备高宽，像素比
                    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) " # 通过user agent代理来模拟
                    "AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"}
    chrome_options = Options() 
    chrome_options.add_argument('disable-infobars')
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = webdriver.Chrome(chrome_options = chrome_options) 
    return driver

#获取股票代码以及名字
def get_shares_code():
    basic=ts.get_stock_basics()
    code_list=basic.index.tolist()#通过其索引得到股票代码
    code_name=basic['name'].tolist()#得到里面的name元素,即股票名称
    return code_list,code_name

#得到股票代码,股票名字,并定义必须元素    
code_list,code_name=get_shares_code()
my_code_data_list=[]
my_code_data=pd.DataFrame()
my_code_data['code']=code_list
my_code_data['code_name']=code_name

basic_url='http://m.emoney.cn/sosoSD/test_pub.html?sc=%s'
new_url_list=[]
for index,value in enumerate(code_list):
    new_url=basic_url % value
    #print (new_url)
    new_url_list.append(new_url)


driver1 = simulator_driver()
driver2 = mobile_driver()
code_rank=[]

num=320
i=num
#for index,value in enumerate(new_url_list):
for aaa in range(len(new_url_list)):
    tmp_data={}
    url=new_url_list[aaa+num-1]
    if i>361:
        break
    tmp= i%2
    if tmp == 0:
        driver1.get(url)
        time.sleep(1.1)
        try:
            tmp_code_name=driver1.find_elements_by_xpath ('//*[@id="TestPubSN"]/span[1]')[0].text
            rank=driver1.find_elements_by_xpath ('//*[@id="TestPubSN"]/span[2]')[0].text
            print ('当前股票 %s 股票名字 %s 评级为: %s .............. i =%d , i的余数为 %d' % (url[-6:],tmp_code_name,rank,i,tmp))
            code_rank.append(rank)
            tmp_data['code_rank']=rank
        except Exception as e:
            print(e)
            print('当前股票 %s 没有获取成功' % url[-6:])
            code_rank.append('000') 
            tmp_data['code_rank']='000'
    else:
        driver2.get(url)
        time.sleep(1.1)
        try:
            tmp_code_name=driver2.find_elements_by_xpath ('//*[@id="TestPubSN"]/span[1]')[0].text
            rank=driver2.find_elements_by_xpath ('//*[@id="TestPubSN"]/span[2]')[0].text
            print ('当前股票 %s 股票名字 %s 评级为: %s .............. i =%d , i的余数为 %d' % (url[-6:],tmp_code_name,rank,i,tmp))
            code_rank.append(rank)
            tmp_data['code_rank']=rank
        except Exception as  e:
            print(e)
            print('当前股票 %s 没有获取成功' % url[-6:])
            code_rank.append('000') 
            tmp_data['code_rank']='000'
    my_code_data_list.append(tmp_data)
    i +=1

print (code_rank)
print (my_code_data_list)


driver1.quit()
driver2.quit()

#my_code_data['code_rank']=code_rank

#print (my_code_data)

