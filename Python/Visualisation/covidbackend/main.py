from flask import Blueprint
from flask import jsonify,request
import pandas as pd
from .extensions import mongo
from sklearn.cluster import KMeans
from pandas import DataFrame
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from datetime import datetime as dt
from bson.json_util import dumps
main = Blueprint('main', __name__)

@main.route('/',methods=['GET']) 
def index():
    covid_collection = mongo.db.dailycases
    output= []
    for c in covid_collection.find():
        output.append({''})
    return jsonify({'result' : output})

@main.route('/country',methods=['GET']) 
def getcontries():
    covid_collection = mongo.db.statistics
    data= covid_collection.find().distinct('location')
    #print(data)
    return jsonify({'result' : data})

@main.route('/newcases/<country>',methods=['GET']) 
def getcases(country):
    country = country
    covid_collection = mongo.db.statistics
    query = {}
    query["location"] = country
    projection = {}

    projection["total_cases"] = u"$total_cases"
    projection["date"] = u"$date"
    projection["_id"] = 0
    cursor = covid_collection.find(query, projection = projection)
    #print(cursor)
    return dumps(cursor)

@main.route('/deaths', methods=['GET'])
def deaths():
    covid_collection = mongo.db.casescountry
    output= []
    for c in covid_collection.find():
        output.append({'Country': c['Country_Region'], 'deaths':c['Deaths'] })
    return jsonify({'result' : output})
@main.route('/totalconfirmed', methods=['GET'])
def confirmed():
    covid_collection = mongo.db.casescountry
    output= []
    for c in covid_collection.find():
        output.append({'Country': c['Country_Region'], 'Confirmed_cases':c['Confirmed'] })
    return jsonify({'result' : output})

@main.route('/clustering', methods=['GET'])
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
    #print(prediction)
    #print(model.labels_)
    for m,c in zip(model.labels_, covid_collection.find()):
            country.append({'code': c['ISO3'],'name': c['Country_Region'], 'value': m.tolist()})
    return ({'result' : country})

@main.route('/predict', methods=['GET'])
def predict():
    covid_collection=mongo.db.worldcases
    dataframe=pd.DataFrame(list(covid_collection.find()))
    dataframe['CurrentDate']=pd.to_datetime(dataframe['CurrentDate'])
    X=dataframe['CurrentDate'].values
    Y=dataframe['Total Deaths'].values
    X=X.reshape(1,-1)
    X=X.reshape(X.shape[0:])
    X=X.transpose()
    X_train,X_test,Y_train,Y_test=train_test_split(X, Y, test_size=0.5,random_state=0)
    X_train=StandardScaler().fit_transform(X_train)
    X_test=StandardScaler().fit_transform(X_test)
    reg=LinearRegression()
    reg.fit(X_train,Y_train)
    Y_pred=reg.predict(X_test)
    dff=pd.DataFrame({'Actual':Y_test.flatten(),'Predicted':Y_pred.flatten()})
    dict=dff.to_dict('records')
    #print(dataframe['CurrentDate'].values)
    return ({'result' : dict, 'date':'2020-01-23'})


