# -*- coding: utf-8 -*-

import tushare as ts
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pandas
#导入本地IP池
from ips import _get_ip


def simulator_driver():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    #chrome_options.add_argument('--proxy-server=http://%s' % _get_ip())
    driver = webdriver.Chrome(chrome_options=chrome_options)
    return driver
    
def mobile_driver():
    mobile_emulation = {"deviceMetrics": {"width": 750, "height": 1334, "pixelRatio": 6.0}, # 定义设备高宽，像素比
                    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) " # 通过user agent代理来模拟
                    "AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"}
    chrome_options = Options() 
    chrome_options.add_argument('disable-infobars')
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = webdriver.Chrome(chrome_options = chrome_options) 
    return driver


def get_shares_code():
    basic=ts.get_stock_basics()
    code_list=basic.index.tolist()
    code_name=basic['name'].tolist
    return code_list,code_name
    
code_name,code_list=get_shares_code()
my_code_data_list=[]
my_code_data=pd.DaaFrame()
my_code_data['code']=code_list
my_code_data['code_name']=code_name

basic_url='http://m.emoney.cn/sosoSD/test_pub.html?sc=%s'
new_url_list=[]
for index,value in enumerate(code_list):
    new_url=basic_url % value
    #print (new_url)
    new_url_list.append(new_url)
print (new_url_list)



driver1 = simulator_driver()
driver2 = mobile_driver()
code_rank=[]
i=1
#for index,value in enumerate(new_url_list):
for aaa in range(len(new_url_list)):
    tmp_data={}
    url=new_url_list[aaa]
    if i>199:
        break
    tmp= i%2
    if tmp == 0:
        driver1.get(url)
        time.sleep(1.1)
        try:
            rank=driver1.find_elements_by_xpath ('//*[@id="TestPubSN"]/span[2]')[0].text
            print ('当前股票 %s  评级为: %s .............. i =%d , i的余数为 %d' % (url[-6:],rank,i,tmp))
            code_rank.append(rank)
            tmp_data['code_rank']=rank
        except:
            print('当前股票 %s 没有获取成功' % url[-6:])
            code_rank.append('000') 
            tmp_data['code_rank']='000'
    else:
        driver2.get(url)
        time.sleep(1.1)
        try:
            rank=driver2.find_elements_by_xpath ('//*[@id="TestPubSN"]/span[2]')[0].text
            print ('当前股票 %s  评级为: %s .............. i =%d , i的余数为 %d' % (url[-6:],rank,i,tmp))
            code_rank.append(rank)
            tmp_data['code_rank']=rank
        except:
            print('当前股票 %s 没有获取成功' % url[-6:])
            code_rank.append('000') 
            tmp_data['code_rank']='000'
    my_code_data_list.append(tmp_data)
    i +=1

print (code_rank)


driver1.quit()
driver2.quit()

my_code_data['code_rank']=code_rank
print (my_code_data)
