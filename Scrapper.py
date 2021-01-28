from selenium import webdriver
import pandas as pd
from time import sleep

import requests
from bs4 import BeautifulSoup

import sqlite3 as sql





url="https://www.etsy.com/in-en/listing/171816901/12-carat-gold-diamond-earrings-14k-white?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=sr_gallery-1-8&frs=1"
driver =  webdriver.Chrome(executable_path=r'C:\Users\chromedriver')
driver.get(url)

source = requests.get(url).text
soup = BeautifulSoup(source,"lxml")




X=[] 
page= driver.find_element_by_xpath('//*[@id="reviews"]/div[2]/nav/ul/li[position() = last()]/a')

for j in range (0,14):
    
    for i in range(0,4):
        review_part=driver.find_element_by_xpath('//*[@id="review-preview-toggle-'+str(i)+'"]')        
        X.append(review_part.text.strip())
        
    #myreviewxpath//*[@id="review-preview-toggle-0"]
    page= driver.find_element_by_xpath('//*[@id="reviews"]/div[2]/nav/ul/li[position() = last()]/a')
    page.click()                         
    sleep(5)






df1 =pd.DataFrame()
df1['reviews_df'] = X
df1.to_csv('newreview.csv', index = False)
conn = sql.connect('newreview.db')
df1.to_sql('review', conn , index=False)















