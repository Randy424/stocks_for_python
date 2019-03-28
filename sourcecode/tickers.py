#!/usr/bin/python

import json
import pandas as pd 
import requests
import re
from iex import Stock
import os
import sys

#sys.argv[1] = size
#sys.argv[2] = file name

def save_tickers(n):
   """ 
   Sends get request to url, calls get_tickers to #parses html, 
   and return 'n' tickers. 
   If tickers.txt does not already exist, function creates
   it; otherwise it is appended to. 
   Appends tickers, one per line. 
   Returns the get request text body. 
   """

   headers = {'Accept-Encoding': 'identity'}
   r = requests.get("http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQrender=download",
   headers=headers)

   ticker_list = get_tickers(r, n)

   if(len(ticker_list) > 0):
      if (os.path.isfile(sys.argv[2])):
         f = open(sys.argv[2], "a+")
      else:
         f = open(sys.argv[2], "w+")

      for i in ticker_list:
         if confirm_ticker(i):
            f.write( f"{i.upper()} \n")
      f.close()
   else:
      print("requesting too many tickers, n =< 150")
   return r

def get_tickers(html, n):
   """
   Parses html from request.get() output
   returns list of 'n' many tickers
   """
   #isolating ticker from url
   results = re.findall(r'/symbol/.*" ', html.text)
   ticker_list = []

   priorurl = html
   while n>len(results):
         nexturl = re.findall(r"https://.*id=\Wmain_content_lb_NextPage",priorurl.text)
         nurl_list = nexturl[0].split()
         nextpage = nurl_list[len(nurl_list)-2]
         nextpage = re.findall(r'https://.*[^"]',nextpage)
         nexturl = requests.get(nextpage[0])
         priorurl=nexturl
         results+=re.findall(r'/symbol/.*" ', nexturl.text)

   #if n > limit, returns empty list
   if n > len(results):
      return ticker_list

   #parsing text, storing possible tickers
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
   inpt = int(sys.argv[1])
   save_tickers(inpt)

