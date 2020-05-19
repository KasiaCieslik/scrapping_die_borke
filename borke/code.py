#!/usr/bin/env python
# coding: utf-8

# In[12]:
import time
import requests
from bs4 import BeautifulSoup
from dateutil import parser
import re
import pandas as pd
import os.path


# In[123]:

def extract_float_from_string(string):
    l = [float(x) for x in re.findall("\d+\.\d+", string)]
    if len(l) == 1:
        return l[0]
    else:
        return l

url = 'https://www.surf-und-segelschule-mueggelsee.de/?Wetterdaten'

def download_weather_data(url):
    response = requests.get(url) # 
    html = response.content
    scraped = BeautifulSoup(html,'html.parser')
    return scraped


# In[125]:

def parse_data(scraped):
    d = []
    for data in scraped.find('div',class_="tbis-layout-cell layout-item-old-1").find_all('tr'):
        d.append(data.text)
    mapping = {}
    mapping['lastupdate'] = parser.parse(d[0].split(': ')[1])
    mapping['temp'] = extract_float_from_string(d[2])
    mapping['wind'] = extract_float_from_string(d[3])[0]
    mapping['boen'] = extract_float_from_string(d[3])[1]
    mapping['niederschlag'] = extract_float_from_string(d[4])
    mapping['feuchte'] = int(re.findall("\d+\\d+", d[5])[0])
    mapping['luftdruck'] = extract_float_from_string(d[6])
    return mapping


# In[127]:

def save_data(mapping,file_name=r'C:\Users\kk\Documents\Python Projects\scrapping_die_borke\results\weather.csv'):
    mapping_csv = pd.DataFrame.from_records([mapping])
    if os.path.isfile(file_name):
        mapping_csv.to_csv(file_name,mode='a',header=None)
    else:
        mapping_csv.to_csv(file_name,mode='a')


# In[129]:


def get_data(url):
    scraped = download_weather_data(url)
    mapping = parse_data(scraped)
    save_data(mapping)


while True:
    get_data(url)
    time.sleep(60)


# In[132]:


#import time
#while True:
 #   try:
  #  get_data(url)
   # time.sleep(60*10)
    #except Exception as e:
     #   print("File not accessible",e)



