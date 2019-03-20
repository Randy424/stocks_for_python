import sys
import csv
import sklearn

def predictor(ticker,infofile,graphfile,col,t):
    """
    Gets the various col values for ticker and stores it in
    col_data
    """
    col_data = []
    reader = csv.DictReader(open(infofile,"r"), delimiter = ',')
    for row in reader:
        if row["Ticker"] == ticker:
            col_data.append(row[col])

if __name__ == "__main__":
    predictor(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5])
