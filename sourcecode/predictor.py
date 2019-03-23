import sys
import csv
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model,model_selection
from sklearn.preprocessing import LabelEncoder
import datetime

def predictor(ticker,infofile,graphfile,col,t):
    """
    Gets the various time and col values for ticker and stores it in
    time_data and col_data respectively
    """
    start_time = datetime.datetime.now()
    time_data = []
    col_data = []
    test_time = []
    predictions = []

    #get values from csv file
    reader = csv.DictReader(open(infofile,"r"), delimiter = ',')
    for row in reader:
        if row["Ticker"] == ticker:
            time_data.append(row["Time"])
            col_data.append(row[col])

    #sets up linear regression model
    #time_data_encoded = LabelEncoder().fit_transform(time_data)
    #model = linear_model.LinearRegression()
    #model.fit(time_data_encoded,col_data)
    #model.fit(time_data,col_data)

    #goes through prediction loop 
    for i in range(t):
        currentDT = start_time.replace(minute=start_time.minute+(i+1))
        test_time.append(currentDT.strftime('%H:%M'))
        #predictions.append(model.predict(test_time))
        predictions.append(col_data[0])

    #output graph with historical data and predicted data. Color seperated
    show_graph(time_data,col_data,test_time,predictions)

def show_graph(time,results,pred_time,pred_results):
    """
    Displays graph based on time and col historical data as well as the
    predicted results from the linear regression model
    """
    #plt.scatter(x,y)
    #plt.show()
    graph = plt.figure()
    ax = graph.add_subplot(1,1,1)
    ax.plot(time,results,'r',pred_time,pred_results,'b')
    plt.show()

if __name__ == "__main__":
    predictor(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],int(sys.argv[5]))
