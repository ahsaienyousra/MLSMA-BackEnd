# importing modules
import requests
import pandas as pd 
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from pymongo import MongoClient
import csv
import json
import os

# requesting data from website
url = 'https://www.worldometers.info/coronavirus/coronavirus-death-toll/?fbclid=IwAR3gYa5QMjBbdxQXjATiyrxxdBJIpA5Etidcgov7DH3h8IhliDi1k8KT2WA'
r = requests.get(url)

# parsing it to beautiful soup
data = r.text
soup = BeautifulSoup(data,'html.parser')

# Printing basic data
#print(soup.title.text)
#print()
#live_data = soup.find_all('div',id='maincounter-wrap')
#for i in live_data:
#	print(i.text)

#print()
#print('Analysis based on individual countries')
#print()

# Extracting table data
#table = soup.find('div',id='maincounter-wrap')
table_body = soup.find('tbody')
table_rows = table_body.find_all('tr')

Date = []
Total_Deaths = []
change_in_total = []
#pourcentage_change = []

for tr in table_rows:
	td = tr.find_all('td')
	Date.append(td[0].text.strip()+". 2020")
	Total_Deaths.append(td[1].text)
	change_in_total.append(td[2].text.strip())
    #pourcentage_change.append(td[3].text)
	

#indices = [i for i in range(1,len(Country_Region)+1)]
headers = ['Date','Total_Deaths','change_in_total']
df = pd.DataFrame(list(zip(Date,Total_Deaths,change_in_total)),columns=headers)

print(df)

# Saving it to csv file

df.to_csv('C:\\Users\\HP\\deaths-corona.csv')
df.to_json('C:\\Users\\HP\\deaths-corona.json')