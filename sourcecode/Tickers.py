import json
import pandas as pd 
import requests


def save_tickers(n):
   headers = {'Accept-Encoding': 'identity'}
   r = requests.get("http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQrender=download",
   headers=headers)
   return r

if __name__=="__main__":
    print (save_tickers(0).text)