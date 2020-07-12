# importing modules
import requests
import pandas as pd 
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from pymongo import MongoClient
import csv
import json
import os
df = pd.read_csv('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv?fbclid=IwAR0V8qbQlnxFWhHn271xXzpk13vHG7U50F1Dq0VKMcp_zPw9IHGqZj12ptg')
df.to_csv('C:\\Users\\HP\\statistics.csv')
df.to_json('C:\\Users\\HP\\statistics.json')
print(df)