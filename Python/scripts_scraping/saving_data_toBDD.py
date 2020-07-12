# importing modules
import requests
import pandas as pd 
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from pymongo import MongoClient
import csv
import json
import os


# Saving it to mongodb
# Charger le fichier CSV
fcsv = 'C:\\Users\\HP\\casescountry.csv'
#charger le repertoire ou le fichier JSON creer sera enregistrer
fjson = 'C:\\Users\\HP\\casescountry.json'
data = []
with open(fcsv) as csvfile:
    reader = csv.DictReader(csvfile)
    for rows in reader:
        data.append(rows)
# Enregistrer le fichier JSON
with open(fjson, 'w') as jsonFile:
    jsonFile.write(json.dumps(data, indent=2))
print("JSON enregistré!")
#Importer le fichier JSON sur MongoDB
client = MongoClient('localhost', 27017)
db = client['covid19'] #remplacer par le nom de la base
collection_currency = db['casescountry']#remplacer /nom collection
with open(fjson) as f:
    file_data = json.load(f)
# utiliser collection_currency.insert(file_data) si la version de pymongo est < 3.0
collection_currency.insert_many(file_data)
client.close()
print('Fichier casescountry Importé avec succes!!')


#********************************************************#
# Saving it to mongodb
# Charger le fichier CSV
fcsv = 'C:\\Users\\HP\\statistics.csv'
#charger le repertoire ou le fichier JSON creer sera enregistrer
fjson = 'C:\\Users\\HP\\statistics.json'
data = []
with open(fcsv) as csvfile:
    reader = csv.DictReader(csvfile)
    for rows in reader:
        data.append(rows)
# Enregistrer le fichier JSON
with open(fjson, 'w') as jsonFile:
    jsonFile.write(json.dumps(data, indent=2))
print("JSON enregistré!")
#Importer le fichier JSON sur MongoDB
#client = MongoClient('localhost', 27017)
db = client['covid19'] #remplacer par le nom de la base
collection_currency = db['statistics']#remplacer /nom collection
with open(fjson) as f:
    file_data = json.load(f)
# utiliser collection_currency.insert(file_data) si la version de pymongo est < 3.0
collection_currency.insert_many(file_data)
client.close()
print('Fichier statistics Importé avec succes!!')

#**************************************************************************#
# Saving it to mongodb
# Charger le fichier CSV
fcsv = 'C:\\Users\\HP\\deaths-corona.csv'
#charger le repertoire ou le fichier JSON creer sera enregistrer
fjson = 'C:\\Users\\HP\\deaths-corona.json'
data = []
with open(fcsv) as csvfile:
    reader = csv.DictReader(csvfile)
    for rows in reader:
        data.append(rows)
# Enregistrer le fichier JSON
with open(fjson, 'w') as jsonFile:
    jsonFile.write(json.dumps(data, indent=2))
print("JSON enregistré!")
#Importer le fichier JSON sur MongoDB
client = MongoClient('localhost', 27017)
#db = client['covid19'] #remplacer par le nom de la base
collection_currency = db['deaths']#remplacer /nom collection
with open(fjson) as f:
    file_data = json.load(f)
# utiliser collection_currency.insert(file_data) si la version de pymongo est < 3.0
collection_currency.insert_many(file_data)
client.close()
print('Fichier deaths-corona Importé avec succes!!')