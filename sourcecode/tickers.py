import json
import pandas as pd 
import requests
import re
from iex import Stock
import os
import sys


def save_tickers(n):
   """ 
   Sends get request to url, parses html and return 'n' tickers 
   """
   headers = {'Accept-Encoding': 'identity'}
   r = requests.get("http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQrender=download",
   headers=headers)
   ticker_list = get_tickers(r, n)
   if(len(ticker_list) > 0):
      if (os.path.isfile("./tickers.txt")):
         f = open("./tickers.txt", "a+")
      else:
         f = open("./tickers.txt", "w+")
   
      for i in ticker_list:
         if(confirm_ticker):
            f.write( f"{i} \n")
      f.close()
   else: 
      print("requesting too many tickers, n =< 50")
   return r

def get_tickers(html, n):
   """
   Parses html and returns list of 'n' tickers
   """
   #isolating ticker from url
   results = re.findall(r'/symbol/.*" ', html.text)
   ticker_list = []
   if n > len(results):
      return ticker_list
   else:
      for i in range(n):
         temp = results[i].split("\" ")
         splitr = temp[0].split('/')
         ticker = splitr[2]
         ticker_list.append(ticker)
   return ticker_list

def confirm_ticker(t):
   """
   Uses iex.Stock().price to check if a ticker has a listed price
   """
   try:
      #blocking std output from Stock().price()
      blockPrint()

      #checking if ticker has price
      Stock(t).price()

      #Restoring std output
      enablePrint()

      return True
   except:
    #print("Unexpected error:", sys.exc_info()[0])
    #print(f"Ticker: {t} not found")
    return False


def blockPrint():
   """
   Disable stdoutput
   """
   sys.stdout = open(os.devnull, 'w')

def enablePrint():
   """
   Restore stdoutput
   """
   sys.stdout = sys.__stdout__


if __name__=="__main__":
  pass