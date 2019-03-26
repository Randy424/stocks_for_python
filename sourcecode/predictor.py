import sys
import csv
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model,model_selection
from sklearn.preprocessing import LabelEncoder, Normalizer
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

    model = linear_model.LinearRegression()

    time_data_encoded = LabelEncoder().fit_transform(time_data)
    col_data_encoded = LabelEncoder().fit_transform(col_data)

    time_data_encoded = np.array(time_data_encoded).reshape(-1,1)
    col_data_encoded = np.array(col_data_encoded).reshape(-1,1)

    model.fit(time_data_encoded,col_data_encoded)

    #finds times to evaluate
    for i in range(t):
        currentDT = start_time + datetime.timedelta(seconds=60*(i+1))
        test_time.append(currentDT.strftime('%H:%M'))

    #goes through prediction loop
    test_time_encoded = LabelEncoder().fit_transform(test_time)
    test_time_encoded = np.array(test_time_encoded).reshape(-1,1)
    predictions = model.predict(test_time_encoded)
    #print(test_time)
    #print(test_time_encoded)
    #for outer in test_time_encoded:
    #    for time in test_time_encoded(outer):
    #        predictions.append(model.predict(time))

    #output graph with historical data and predicted data. Color seperated
    save_graph(time_data,col_data,test_time,predictions)

def save_graph(time,results,pred_time,pred_results):
    """
    Displays graph based on time and col historical data as well as the
    predicted results from the linear regression model
    """
    #plt.scatter(x,y)
    #plt.show()
    graph = plt.figure()
    ax = graph.add_subplot(1,1,1)
    ax.plot(time,results,'r',pred_time,pred_results,'b')
    plt.xlabel("Time")
    plt.ylabel(sys.argv[4])

    #saves graph
    plt.savefig(sys.argv[3]+".png")


if __name__ == "__main__":
    predictor(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],int(sys.argv[5]))
