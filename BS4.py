# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 13:48:27 2023

@author: user
"""

import requests 
from bs4 import BeautifulSoup
import pandas as pd

url="https://tabelog.com/tw/tokyo/rstLst/"
res=requests.get(url)
soup=BeautifulSoup(res.text,"html.parser")
#print(soup)
tags=soup.find_all("li",class_="list-rst js-list-item")
restaurant=[]
mprice=[]
nprice=[]
rearaurant=[]
eva=[]
item=[]
mprice=[]
nprice=[]
for tag in tags:
   # print(tag.find('a').text)
    #print(tag.find('b',).text) #評價
    #print(tag.find_all('span',class_="c-rating__val")[0].text)
   # print(tag.find_all('span',class_="c-rating__val")[1].text)
    #print(tag.find("li",class_="list-rst__catg").text)
    restaurant.append(tag.find('a').text)
    eva.append(tag.find('b',).text)
    mprice.append(tag.find_all('span',class_="c-rating__val")[0].text)
    nprice.append(tag.find_all('span',class_="c-rating__val")[1].text)
    item.append(tag.find("li",class_="list-rst__catg").text)
    
    
columns=["評價","中餐價格","晚餐價格","品項"]
data=[eva,mprice,nprice,item]
df = pd.DataFrame(data,index=columns ,columns=restaurant).T
df.to_csv("out4_50b.csv",encoding="utf_8_sig")
