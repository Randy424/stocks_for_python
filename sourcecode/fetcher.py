import os
import sys
import csv
import pandas as pd
import datetime
import time
from iex import Stock

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
        f = open('tickers.txt', 'r')
    
        header=['Time', 'Ticker', 'latestPrice',
        'latestVolume', 'Close', 'Open', 'low', 'high']

        if (os.path.isfile("./info.csv") == False):
            f_info = open("./info.csv", "w+")
            writer = csv.DictWriter(f_info, fieldnames=header)
            writer.writeheader()
            f_info.close()

        for l in f:
            l = l.strip()
            write_update(l)

def write_update(ticker):
    """
    Is called from gettickers_callupdate()
    Gets current stock quote using ticker (ticker symbol as string)
    if ticker exists in pdf, updates ticker, if not, it appends current quote
    data is saved via overwriting previous info.csv 

    args: ticker - string

    """
    
    header=['Time', 'Ticker', 'latestPrice',
    'latestVolume', 'Close', 'Open', 'low', 'high']

    book = get_book(ticker)

    data = pd.read_csv("./info.csv", usecols=header) 
    
    written = False
    for index, row in data.iterrows():
        if row['Ticker'] == ticker:
            #df1.loc[df1['stream'] == 2, ['feat','another_feat']] = 'aaaa'
            print("Ticker", row['Ticker'])
            data.loc[data['Ticker']== ticker, ['Time', 'latestPrice', 'latestVolume',
            'Close', 'Open', 'low', 'high']] = get_time(),book['latestPrice'], book['latestVolume'], book['close'], book['open'],book['low'], book['high']
            written = True
    
    if written == False:
        df_x = pd.DataFrame([[get_time(),book['symbol'],book['latestPrice'],book['latestVolume'],
            book['close'], book['open'],book['low'], book['high']]], columns=header)
        data = data.append(df_x)

    data.to_csv("./info.csv", index = False)
    #print(data)


#returns time in needed format for csv 
def get_time():
    currentDT = datetime.datetime.now()
    return currentDT.strftime('%H:%M')

#returns stock information in the form of a dicitonary
def get_book(ticker):
    book = Stock(ticker).quote()
    
    #print(book)
    return book

#for testing, we can get rid of this later
def test_reader():
    reader = csv.DictReader(open("./info.csv", "r"), delimiter=',')

    for row in reader:
        print(row)    

if __name__ == '__main__':
    gettickers_callupdate(10)
