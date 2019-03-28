#Python Programming, Spring 2019

#README for Programming Project I, stocks_for_python
    Due: March 28th, 2019, 11:59PM
    sumbmission file: piverger_ali.tar
    included .py files: tickers.py, fetcher.py, query.py, predictor.py
    Git Hub link: https://github.com/Randy424/stocks_for_python
    Git Hub invite link: https://github.com/Randy424/stocks_for_python/invitations

#Usage:
    stocks_for_python is a collection of python scripts that can fetch an inputed 
    number of stock tickers from the nasdaq exchange website (http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQrender=download)

#tickers.py: 
    Run from command line with: python3 tickers.py number_of_tickers ticker filename

    The script creates file, 'filename', then prints the first n, 'number_of_tickers',
    VALID tickers to the file. It confirms the tickers validity using iex-api-python's
    price() function. Script uses the requests module to pull the html from the nasdeq's public website (http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQrender=download) and a regular expression operation to parse 
    ticker names. 

#fetcher.py:
    Run from command line with: python3 fetcher.py time_lim ticker_filename info_filename

    The script opens file, 'ticker_filename', (output from tickers.py), reads tickers one by one over the specified time limit 'time_lim', uses the iex-api-python module to request ticker information though its 'quote()' function, then opens a new file 'info_filename', and stores 'Time', 'Ticker', 'latestPrice', 'latestVolume', 'Close', 'Open', 'low', 'high' in a csv form. Script will continue to append recent stock information every minute until time_lim is reached. 

#query.py:
    Run from command line with: 
    python3 query.py –verbose True/False –file info_filename –ticker ticker –time time
    
    A module function that takes the information file name,'info_filename', time, 'time' and ticker, 'ticker' as input.

    

