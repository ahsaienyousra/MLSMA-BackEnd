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
url = 'https://github.com/CSSEGISandData/COVID-19/blob/web-data/data/cases_country.csv?fbclid=IwAR069_Fi-OR0kzOl3oUVZPFE1qWxAVFegaGdejKLyMg6UY35bo04NoscAyo'
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
table_body = soup.find('tbody')
table_rows = table_body.find_all('tr')

Country_Region = []
Last_Update = []
Lat = []
Long_ = []
Confirmed = []
Deaths = []
Recovered = []
Active = []
Incident_Rate = []
People_Tested = []
People_Hospitalized = []
Mortality_Rate = []
UID = []
ISO3 = []
for tr in table_rows:
	td = tr.find_all('td')
	Country_Region.append(td[1].text)
	Last_Update.append(td[2].text)
	Lat.append(td[3].text.strip())
	Long_.append(td[4].text.strip())
	Confirmed.append(td[5].text.strip())
	Deaths.append(td[6].text)
	Recovered.append(td[7].text)
	Active.append(td[8].text.strip())
	Incident_Rate.append(td[9].text.strip())
	People_Tested.append(td[10].text.strip())
	People_Hospitalized.append(td[11].text)
	Mortality_Rate.append(td[12].text.strip())
	UID.append(td[13].text.strip())
	ISO3.append(td[14].text.strip())

indices = [i for i in range(1,len(Country_Region)+1)]
headers = ['Country_Region','Last_Update','Lat','Long_','Confirmed','Deaths','Recovered','Active','Incident_Rate','People_Tested','People_Hospitalized','Mortality_Rate','UID','ISO3']
df = pd.DataFrame(list(zip(Country_Region,Last_Update,Lat,Long_,Confirmed,Deaths,Recovered,Active,Incident_Rate,People_Tested,People_Hospitalized,Mortality_Rate,UID,ISO3)),index=indices,columns=headers)

print(df)

# Saving it to csv file

df.to_csv('C:\\Users\\HP\\casescountry.csv')
df.to_json('C:\\Users\\HP\\casescountry.json')