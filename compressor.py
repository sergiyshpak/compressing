# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 15:51:53 2018

@author: g705586
"""
import requests
import xml.etree.ElementTree as ET

systemDict= {} 
typesDict=  {}

with open("mapSolarSystems.csv", "r") as ins:
    for line in ins:
        my_list = line.split(",")
        #print(my_list[2]+"   " +my_list[3])
        systemDict[my_list[2]] = my_list[3]

with open("invTypes.csv", "r") as ins:
    for line in ins:
        my_list = line.split(",")
        typesDict[my_list[0]] = my_list[2]

uncompressList = [17471]
compressList = [28431]

pairs=[[17471,28431]]

sell_sysa=30000142

sellurl1 = 'https://api.evemarketer.com/ec/marketstat?typeid='
sellurl2 = '&usesystem='+str(sell_sysa)   
headers = {'user-agent': 'my-app-test/0.0.1'}
    
    
for item in pairs:
    regular=item[0]
    compr=item[1]
    sellurl=sellurl1+str(compr)+sellurl2
    r = requests.get(sellurl, headers=headers)
    print(r.text)
    
    root = ET.fromstring(r.text)

    print('Item  item is '+typesDict.get(compr))
    
    buyMax=root[0][0][0][5]
    print(' buy max ' +str(buyMax.text))
    
    #print(root.find('./exec_api/marketstat/type/buy/max' ))
   # print(root.find('./exec_api' ).text)
    