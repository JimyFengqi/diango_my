#coding:utf-8
import time  
from selenium import webdriver  

'''
webdriver模拟手机行为
第一种方法是通过device name来确定我们要模拟的手机样式
第二种 可以直接指定分辨率以及UA标识，然后模拟手机

'''
device_names=[
"Apple iPhone 3GS",
 "Apple iPhone 4",
 "Apple iPhone 5",
 "Apple iPhone 6",
 "Apple iPhone 6 Plus",
 "BlackBerry Z10",
 "BlackBerry Z30",
 "Google Nexus 4",
 "Google Nexus 5",
 "Google Nexus S",
 "HTC Evo, Touch HD, Desire HD, Desire",
 "HTC One X, EVO LTE",
 "HTC Sensation, Evo 3D",
 "LG Optimus 2X, Optimus 3D, Optimus Black",
 "LG Optimus G",
 "LG Optimus LTE, Optimus 4X HD" ,
 "LG Optimus One",
 "Motorola Defy, Droid, Droid X, Milestone",
 "Motorola Droid 3, Droid 4, Droid Razr, Atrix 4G, Atrix 2",
 "Motorola Droid Razr HD",
 "Nokia C5, C6, C7, N97, N8, X7",
 "Nokia Lumia 7X0, Lumia 8XX, Lumia 900, N800, N810, N900",
 "Samsung Galaxy Note 3",
 "Samsung Galaxy Note II",
 "Samsung Galaxy Note",
 "Samsung Galaxy S III, Galaxy Nexus",
 "Samsung Galaxy S, S II, W",
 "Samsung Galaxy S4",
 "Sony Xperia S, Ion",
 "Sony Xperia Sola, U",
 "Sony Xperia Z, Z1",
 "Amazon Kindle Fire HDX 7",
 "Amazon Kindle Fire HDX 8.9",
 "Amazon Kindle Fire (First Generation)",
 "Apple iPad 1 / 2 / iPad Mini",
 "Apple iPad 3 / 4",
 "BlackBerry PlayBook",
 "Google Nexus 10",
 "Google Nexus 7 2",
 "Google Nexus 7",
 "Motorola Xoom, Xyboard",
 "Samsung Galaxy Tab 7.7, 8.9, 10.1",
 "Samsung Galaxy Tab",
 "iPhone 6",
 "iPhone 7"
]
#第一种方法  
for device_name in device_names:
    mobile_emulation = {"deviceName":device_name} 
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)  
        driver = webdriver.Chrome(chrome_options = chrome_options)
        driver.get("http://www.baidu.com")
        time.sleep(5)  
        driver.close() 
    except Exception as e:
        print(e)


'''

mobile_emulations = {
"deviceName": "Apple iPhone 3GS",
"deviceName": "Apple iPhone 4",
"deviceName": "Apple iPhone 5",
"deviceName": "Apple iPhone 6",
"deviceName": "Apple iPhone 6 Plus",
"deviceName": "BlackBerry Z10",
"deviceName": "BlackBerry Z30",
"deviceName": "Google Nexus 4",
"deviceName": "Google Nexus 5",
"deviceName": "Google Nexus S",
"deviceName": "HTC Evo, Touch HD, Desire HD, Desire",
"deviceName": "HTC One X, EVO LTE",
"deviceName": "HTC Sensation, Evo 3D",
"deviceName": "LG Optimus 2X, Optimus 3D, Optimus Black",
"deviceName": "LG Optimus G",
"deviceName": "LG Optimus LTE, Optimus 4X HD" ,
"deviceName": "LG Optimus One",
"deviceName": "Motorola Defy, Droid, Droid X, Milestone",
"deviceName": "Motorola Droid 3, Droid 4, Droid Razr, Atrix 4G, Atrix 2",
"deviceName": "Motorola Droid Razr HD",
"deviceName": "Nokia C5, C6, C7, N97, N8, X7",
"deviceName": "Nokia Lumia 7X0, Lumia 8XX, Lumia 900, N800, N810, N900",
"deviceName": "Samsung Galaxy Note 3",
"deviceName": "Samsung Galaxy Note II",
"deviceName": "Samsung Galaxy Note",
"deviceName": "Samsung Galaxy S III, Galaxy Nexus",
"deviceName": "Samsung Galaxy S, S II, W",
"deviceName": "Samsung Galaxy S4",
"deviceName": "Sony Xperia S, Ion",
"deviceName": "Sony Xperia Sola, U",
"deviceName": "Sony Xperia Z, Z1",
"deviceName": "Amazon Kindle Fire HDX 7″",
"deviceName": "Amazon Kindle Fire HDX 8.9″",
"deviceName": "Amazon Kindle Fire (First Generation)",
"deviceName": "Apple iPad 1 / 2 / iPad Mini",
"deviceName": "Apple iPad 3 / 4",
"deviceName": "BlackBerry PlayBook",
"deviceName": "Google Nexus 10",
"deviceName": "Google Nexus 7 2",
"deviceName": "Google Nexus 7",
"deviceName": "Motorola Xoom, Xyboard",
"deviceName": "Samsung Galaxy Tab 7.7, 8.9, 10.1",
"deviceName": "Samsung Galaxy Tab",
"deviceName": "Notebook with touch",
"deviceName": "iPhone 6"
}



#通过添加add_experimental_option,增加mobile_emulation选项,然后使webdriver模拟手机行为
options.add_experimental_option('mobileEmulation', mobileEmulation)
'''

 

 


#第二种,指定手机分辨率,但是只有分辨率是不行的,还必须指定user-agent

WIDTH = 320
HEIGHT = 640
PIXEL_RATIO = 3.0
UA = 'Mozilla/5.0 (Linux; Android 4.1.1; GT-N7100 Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/6.3'
mobileEmulation = {"deviceMetrics": {"width": WIDTH, "height": HEIGHT, "pixelRatio": PIXEL_RATIO}, "userAgent": UA}# pixelRatio对应分辨率


chrome_options = webdriver.ChromeOptions()  
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)  
driver2 = webdriver.Chrome(chrome_options = chrome_options)
driver.get("http://www.baidu.com")  
time.sleep(5)  
driver.close()  


