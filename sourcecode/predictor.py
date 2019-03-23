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
    hh = start_time.hour
    mm = start_time.minute
    print(start_time)
    print(str(hh) + "\t" + str(mm))
    time_data = []
    col_data = []
    predictions = []

    reader = csv.DictReader(open(infofile,"r"), delimiter = ',')
    for row in reader:
        if row["Ticker"] == ticker:
            time_data.append(row["Time"])
            col_data.append(row[col])

    #time_data_encoded = LabelEncoder().fit_transform(time_data)
    #model = linear_model.LinearRegression()
    #model.fit(time_data_encoded,col_data)
    #for i in range(t):
    #    mm+=1
    #    if mm==60:
    #        hh+=1
    #        mm=0
    #    if hh==24:
    #        hh=0
    #        mm=0
    #    test_time = str(hh)+":"+str(mm)
    #    predictions.append(model.predict(test_time))

    #testing graph purposes!! This section should get removed
    test_time = []
    test_result = []
    for i in range(t):
        mm+=1
        test_time.append(str(hh)+":"+str(mm))
        test_result.append(mm*2)

    #output graph with historical data and predicted data. Color seperated
    show_graph(time_data,col_data,test_time,test_result)

def show_graph(time,results,pred_time,pred_results):
    """
    Displays graph based on x and y input. Will need to add a "second" Y to
    show the historical data
    """
    #plt.scatter(x,y)
    #plt.show()
    graph = plt.figure()
    ax = graph.add_subplot(1,1,1)
    ax.plot(time,results,'r',pred_time,pred_results,'b')
    plt.show()

if __name__ == "__main__":
    predictor(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],int(sys.argv[5]))
