#!/usr/bin/env python
# coding: utf-8

# In[55]:


import csv
import json
from selenium import webdriver
driver = webdriver.Chrome('D:/00課程/大二下學期/競賽/py-crawer/chromedriver.exe')
api_Availability = "https://ptx.transportdata.tw/MOTC/v2/Bike/Availability/Taichung?$format=JSON"

driver.get(api_Availability)


# In[56]:


availability = driver.page_source
print(availability)


# In[57]:


from bs4 import BeautifulSoup
soup_Availability = BeautifulSoup(driver.page_source, 'lxml')
availability_text = soup_Availability.find('pre').text
print(availability_text)

for x in range(1):
# In[58]:
    import datetime
    now = datetime.datetime.now() #現在時間
    date_time = now.strftime("%Y%m%d%H%M%S")
    print(date_time)
# In[59]:
    with open('D:/00課程/大二下學期/競賽/bike-ava-output/availability_data_{}.json'.format(int(date_time)), 'w') as f:
        json.dump(availability_text, f)
    with open('D:/00課程/大二下學期/競賽/bike-ava-output/availability_data_{}.json'.format(int(date_time)), 'r') as f:
        availability_text = json.load(f)
# In[60]:
availability_data = json.loads(availability_text)
print(availability_data)
# In[61]:
    
    with open('D:/00課程/大二下學期/競賽/bike-ava-output/Taichung_Bike_Availibility_{}.csv'.format(int(date_time)), 'w', encoding = 'utf-8', newline = '') as f:
        filewriter = csv.writer(f, delimiter = ',')
        filewriter.writerow(['StationUID', 
                            'ServiceAvailable', 
                            'AvailableRentBikes', 
                            'AvailableReturnBikes', 
                            'SrcUpdateTime'])
    with open('D:/00課程/大二下學期/競賽/bike-ava-output/Taichung_Bike_Availibility_{}.csv'.format(int(date_time)), 'a', encoding = 'utf-8', newline = '') as f:
        filewriter = csv.writer(f, delimiter = ',')
        for i in range(len(availability_data)):
            filewriter.writerow([availability_data[i]['StationUID'], 
                                availability_data[i]['ServiceAvailable'], 
                                availability_data[i]['AvailableRentBikes'], 
                                availability_data[i]['AvailableReturnBikes'], 
                                availability_data[i]['SrcUpdateTime']])


# In[62]:

    driver.close()






