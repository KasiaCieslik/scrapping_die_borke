#!/usr/bin/env python
# coding: utf-8


import time
import requests
from bs4 import BeautifulSoup
from dateutil import parser
import re
import pandas as pd
import os.path
import sqlite3



def extract_float_from_string(string):
    l = [float(x) for x in re.findall("\d+\.\d+", string)]
    if len(l) == 1:
        return l[0]
    else:
        return l


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

def create_db(database_name):
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()
    #cursor.execute('DROP TABLE IF EXISTS weather')
    sql_command = """CREATE TABLE IF NOT EXISTS weather (
    id INTEGER PRIMARY KEY,
    lastupdate DATETIME,
    temp REAL,
    wind REAL,
    boen REAL,
    niederschlag REAL,
    feuchte REAL,
    luftdruck REAL)"""

    cursor.execute(sql_command)
    connection.close()
    
def insert_to_db_table(mapping,database_name):
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()
    sql_command = """INSERT INTO weather 
    (lastupdate, temp, wind, boen, 
    niederschlag, feuchte, luftdruck) 
    VALUES (:lastupdate,:temp,:wind,:boen,
    :niederschlag,:feuchte,:luftdruck)"""

    cursor.execute(sql_command,mapping)
    connection.commit()
    connection.close()

def get_data(url,database_name):
    scraped = download_weather_data(url)
    mapping = parse_data(scraped)
    insert_to_db_table(mapping,database_name)
    




