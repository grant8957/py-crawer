#!/usr/bin/env python
# coding: utf-8

# In[55]:


import json
from selenium import webdriver
driver = webdriver.Chrome()
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


# In[58]:


import datetime
now = datetime.datetime.now() #現在時間

date_time = now.strftime("%Y%m%d%H%M%S")
print(date_time)


# In[59]:


with open('availability_data_{}.json'.format(int(date_time)), 'w') as f:
    json.dump(availability_text, f)

with open('availability_data_{}.json'.format(int(date_time)), 'r') as f:
    availability_text = json.load(f)


# In[60]:


availability_data = json.loads(availability_text)
print(availability_data)


# In[61]:


import csv

with open('Taichung_Bike_Availibility_{}.csv'.format(int(date_time)), 'w', encoding = 'utf-8', newline = '') as f:
    filewriter = csv.writer(f, delimiter = ',')
    filewriter.writerow(['StationUID', 
                         'ServiceAvailable', 
                         'AvailableRentBikes', 
                         'AvailableReturnBikes', 
                         'SrcUpdateTime'])
    
with open('Taichung_Bike_Availibility_{}.csv'.format(int(date_time)), 'a', encoding = 'utf-8', newline = '') as f:
    filewriter = csv.writer(f, delimiter = ',')
    for i in range(len(availability_data)):
        filewriter.writerow([availability_data[i]['StationUID'], 
                             availability_data[i]['ServiceAvailable'], 
                             availability_data[i]['AvailableRentBikes'], 
                             availability_data[i]['AvailableReturnBikes'], 
                             availability_data[i]['SrcUpdateTime']])
###################start
with open('Taichung_Bike_Availibility_All.csv', 'w', encoding = 'utf-8', newline = '') as f:
    filewriter = csv.writer(f, delimiter = ',')
    filewriter.writerow(['StationUID', 
                         'ServiceAvailable', 
                         'AvailableRentBikes', 
                         'AvailableReturnBikes', 
                         'SrcUpdateTime'])
    
with open('Taichung_Bike_Availibility_All.csv', 'a', encoding = 'utf-8', newline = '') as f:
    filewriter = csv.writer(f, delimiter = ',')
    for i in range(len(availability_data)):
        filewriter.writerow([availability_data[i]['StationUID'], 
                             availability_data[i]['ServiceAvailable'], 
                             availability_data[i]['AvailableRentBikes'], 
                             availability_data[i]['AvailableReturnBikes'], 
                             availability_data[i]['SrcUpdateTime']])
####################end


# In[62]:


driver.close()


# In[ ]:




