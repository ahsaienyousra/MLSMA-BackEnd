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
