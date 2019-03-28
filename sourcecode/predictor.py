#!/usr/bin/python

import sys
import csv
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model,model_selection
from sklearn.preprocessing import LabelEncoder, Normalizer
import datetime

"""
"""

def read_csv(infofile, ticker, col):
    """
    Read values from csv
    Returns time data and the requested column data
    """

    time_data = []
    col_data = []

    reader = csv.DictReader(open(infofile,"r"), delimiter = ',')
    for row in reader:
        if row["Ticker"] == ticker:
            time_data.append(row["Time"])
            col_data.append(row[col])

    return time_data, col_data

def build_timedelta(time_data):
    """
    Takes time string and converts it to timedelta and then into seconds
    Returns array of converted seconds
    """
    time_data_seconds = [datetime.datetime.strptime(j, '%H:%M') for j in time_data]
    time_data_seconds = [datetime.timedelta(hours=x.hour, minutes=x.minute).seconds for x in time_data_seconds]

    return time_data_seconds 

def build_test_time_array(time_data, t):
    """
    Builds array of testing values for regression model 
    returns 
    """
    test_time = []
    start_time = datetime.datetime.strptime(time_data[-1], '%H:%M')
    for i in range(t):
        currentDT = start_time + datetime.timedelta(seconds=60*(i+1))
        print (currentDT)
        test_time.append(currentDT.strftime('%H:%M'))
    return test_time

def predictor(ticker,infofile,graphfile,col,t):
    """
    Gets the various time and col values for ticker and stores it in
    time_data and col_data respectively
    """
    #getting time data and column data from helper function
    time_data, col_data = read_csv(infofile, ticker, col)

    #building time delta for training regression model
    time_data_seconds = build_timedelta(time_data) 
    time_data_seconds = np.array(time_data_seconds).reshape(-1,1)

    #sets up linear regression model
    model = linear_model.LinearRegression()
    model.fit(time_data_seconds,col_data)
    
    test_time = build_test_time_array(time_data,t)

    #building time delta for testing regression model
    test_time_seconds = build_timedelta(test_time) 
    test_time_seconds = np.array(test_time_seconds).reshape(t,1)
    
    predictions = model.predict(test_time_seconds)

    print ("time data: ", time_data)
    print ("col data: ", col_data)
    print("predictions: ", predictions)

    save_graph(time_data,col_data,test_time,predictions)

def save_graph(time,results,pred_time,pred_results):
    """
    Displays graph based on time and col historical data as well as the
    predicted results from the linear regression model
    """
    converted_results = [float(item) for item in results]
    converted_predictions = [float(item) for item in pred_results]

    graph = plt.figure()
    ax = graph.add_subplot(1,1,1)
    ax.plot(time, converted_results,'r', pred_time, converted_predictions, 'b')
    plt.xlabel("Time")
    plt.ylabel(sys.argv[4])

    print ("converted results: ",converted_results)
    print("testing graph time: ", time)
    print("testing graph results: ", results)
    
    #Set label and increase font
    graph.suptitle("Predictions for " + sys.argv[1],fontsize=40)
    plt.xlabel("Time", fontsize=20)
    plt.ylabel(sys.argv[4], fontsize=20)

    #Rotates labels on graph
    alltimes = time + pred_time
    allresults = results + list(pred_results)
    plt.xticks(alltimes, [str(i) for i in alltimes], rotation=45)

    #increase graph size
    plt.gcf().set_size_inches(18.5,10)
    #saves graph
    plt.savefig(sys.argv[3]+".png")


if __name__ == "__main__":
    predictor(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],int(sys.argv[5]))
