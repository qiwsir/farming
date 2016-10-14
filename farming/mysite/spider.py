#!#/usr/bin/env python
# coding:utf-8

import sqlite3
import requests
from bs4 import BeautifulSoup
import time

def get_data(url,i):
    req = requests.get(url, i)
    soup = BeautifulSoup(req.text, 'lxml')
    try:
        table = soup.select("#ContentPlaceHolder1_lbldata table table")[0].find_all("td")
        #for j in table:
            #print (j)
        year = str(i)
        province = table[0].find("b").string
        crop = table[6].string
        type_db = table[3].string
        account = str(table[7].string)
        return year, province, crop, type_db, account
    except:
        return False

if __name__ == "__main__":
    for i in range(1949, 2016):
        url = "http://202.127.42.157/moazzys/nongqing_result.aspx?year={}&prov=11%20%20%20&item=02&type=1&radio=1&order1=year_code&order2=prov_code&order3=item_code".format(i)
        result = get_data(url, i)
        if result:
            print(result)
        else:
            print("haha")
        time.sleep(1)


    #conn = sqlite3.connect('/home/asitin/farming/farming/db.sqlite3')