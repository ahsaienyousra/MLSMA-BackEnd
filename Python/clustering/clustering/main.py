from flask import Blueprint
from flask import jsonify
import pandas as pd
from .extensions import mongo
from sklearn.cluster import KMeans
from pandas import DataFrame
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
main = Blueprint('main', __name__)
print("Running on http://127.0.0.1:5000/clustering")
@main.route('/clustering')
def clustering():
    covid_collection=mongo.db.casescountry
    liste=covid_collection.find()
    output=[]
    country=[]
    for c in liste:
        if c['Mortality_Rate']!='':
            output.append([c['Mortality_Rate']])
    scaler = StandardScaler()
    X = scaler.fit_transform(output)
    true_k = 3
    model = KMeans(n_clusters=true_k, init='k-means++')
    model.fit(X)
    order_centroids = model.cluster_centers_.argsort()[:, ::-1]
    Y = scaler.fit_transform([[5.47]])
    prediction = model.predict(Y)
    #covid_colelction['Cluster'].insert_many(labels)
    #covid_colelction.save()
    print(prediction)
    print(model.labels_)
    for m,c in zip(model.labels_, covid_collection.find()):
            country.append([c['Country_Region'], m.tolist()])
    return ({'result' : country})