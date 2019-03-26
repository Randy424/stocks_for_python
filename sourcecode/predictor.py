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

    time_data_encoded = np.array(time_data_encoded).reshape(-1,1)
    col_data_encoded = np.array(col_data).reshape(-1,1)

    model.fit(time_data_encoded,col_data_encoded)

    #KEEP THIS PART FOR SURE
    #Your picture saved values as 00:43 etc instead of 12:43! 
    #finds times to evaluate
    #Use this for time values
    for i in range(t):
        currentDT = start_time + datetime.timedelta(seconds=60*(i+1))
        test_time.append(currentDT.strftime('%H:%M'))

    #goes through prediction loop
    test_time_encoded = LabelEncoder().fit_transform(test_time)
    test_time_encoded = np.array(test_time_encoded).reshape(-1,1)
    predictions = model.predict(test_time_encoded)
    #print(predictions)

    #output graph with historical data and predicted data. Color seperated
    #test_graph(time_data,col_data,test_time,predictions)
    save_graph(time_data,col_data,test_time,predictions)

def save_graph(time,results,pred_time,pred_results):
    """
    Displays graph based on time and col historical data as well as the
    predicted results from the linear regression model
    """
    graph = plt.figure()#(figsize=(4,7),dpi=100)
    ax = graph.add_subplot(1,1,1)
    ax.plot(time,results,'r',pred_time,pred_results,'b')

    #KEEP THE FOLLOWING
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

#THIS IS TRASH
def test_graph(x,y,x2,y2):
    plt.plot(x,y)
    plt.plot(x2,y2)
    plt.show()
if __name__ == "__main__":
    predictor(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],int(sys.argv[5]))
