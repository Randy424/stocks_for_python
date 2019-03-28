import os
import sys
import csv
import pandas as pd
import datetime
import time
from iex import Stock

#sys.argv[1] = time limit
#sys.argv[2] = ticker file
#sys.argv[3] = csv info file
last_ticker_values = {}

def gettickers_callupdate(time_lim):
    """
    Loads tickers from tickers.txt
    if info.csv does not already exist it is created with header
    Calls updater over span of time_lim

    args:
    time_lim - int

    """
    t_end = time.time() + time_lim
    while time.time() < t_end:
        iter_start = datetime.datetime.now()
        f = open(sys.argv[2], 'r')

        header=['Time', 'Ticker', 'latestPrice',
        'latestVolume', 'Close', 'Open', 'low', 'high']

        if (os.path.isfile(sys.argv[3]) == False):
            f_info = open(sys.argv[3], "w+")
            writer = csv.DictWriter(f_info, fieldnames=header)
            writer.writeheader()
            f_info.close()

        #Enter file and grab tickers one by one to update them
        for l in f:
            l = l.strip()
            write_update(l)

        #sleeps the program until the current minute ends
        now = datetime.datetime.now()
        if iter_start.hour == now.hour and iter_start.minute == now.minute:
            time.sleep(60-now.second)

def write_update(ticker):
    """
    Is called from gettickers_callupdate()
    Gets current stock quote using ticker (ticker symbol as string)
    if ticker exists in pdf, updates ticker, if not, it appends current quote
    data is saved via overwriting previous info.csv 

    args: ticker - string

    """
    #print(last_ticker_values)
    header=['Time', 'Ticker', 'latestPrice',
    'latestVolume', 'Close', 'Open', 'low', 'high']

    data = pd.read_csv(sys.argv[3], usecols=header)

    #most recent ticker time is stored in dictionary for faster checking
    if ticker in last_ticker_values:
        if last_ticker_values[ticker] == get_time():
            return

    #Grabs stock information for a ticker and adds it to the dataframe
    book = get_book(ticker)
    df_x = pd.DataFrame([[get_time(),book['symbol'],book['latestPrice'],book['latestVolume'],
        book['close'], book['open'],book['low'], book['high']]], columns=header)
    data = data.append(df_x)

    #updates ticker value in its dictionary
    last_ticker_values[ticker] = get_time()

    data.to_csv(sys.argv[3], index = False)



def get_time():
    """
    returns time in needed format for csv
    """
    currentDT = datetime.datetime.now()
    return currentDT.strftime('%H:%M')

def get_book(ticker):
    """
    returns stock information in the form of a dicitonary
    """
    book = Stock(ticker).quote()

    return book

#for testing, we can get rid of this later
def test_reader():
    reader = csv.DictReader(open(sys.argv[3], "r"), delimiter=',')

    for row in reader:
        print(row)

if __name__ == '__main__':
    gettickers_callupdate(int(sys.argv[1]))

