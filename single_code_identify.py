# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

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
 
def get_code_rank(code):
    basic_url='http://m.emoney.cn/sosoSD/test_pub.html?sc=%s'   
    driver=simulator_driver()
    url=basic_url % code
    driver.get(url)
    time.sleep(1)
    code_name=driver.find_elements_by_xpath ('//*[@id="TestPubSN"]/span[1]')[0].text
    rank=driver.find_elements_by_xpath ('//*[@id="TestPubSN"]/span[2]')[0].text
    print ('当前股票代码 %s 股票名字 %s  评级为: %s .............. ' % (url[-6:],code_name,rank))
    driver.close()
    return rank

code=input('请输入股票代码')
get_code_rank(code)