# stocks_for_python
Python application designed to collect, organize and make predictions on stock behavior. It consists of four separate modules (four .py files). (Project Founders: Taj Ali &amp;  Randy Bruno-Piverger)

#Copy of internal README
#Python Programming, Spring 2019

#README for Programming Project I, stocks_for_python
    Creators: Randy Piverger and Taj Ali
    Due: March 28th, 2019, 11:59PM
    submission file: piverger_ali.tar
    included .py files: tickers.py, fetcher.py, query.py, predictor.py
    Git Hub link: https://github.com/Randy424/stocks_for_python
    Git Hub invite link: https://github.com/Randy424/stocks_for_python/invitations

#Usage:
    stocks_for_python is a collection of python scripts that can fetch an inputed 
    number of stock tickers from the nasdaq exchange website 
    (http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQrender=download)

#tickers.py: 
    Run from command line with: python3 tickers.py number_of_tickers ticker filename

    The script creates file, 'filename', then prints the first n, 'number_of_tickers',
    VALID tickers to the file. It confirms the tickers validity using iex-api-python's
    price() function. Script uses the requests module to pull the html from the nasdeq's 
    public website (http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQrender=download)
    and a regular expression operation to parse ticker names. 

#fetcher.py:
    Run from command line with: python3 fetcher.py time_lim ticker_filename info_filename

    The script opens file, 'ticker_filename', (output from tickers.py), reads tickers one by one over the 
    specified time limit 'time_lim', uses the iex-api-python module to request ticker information though its 'quote()' function, 
    then opens a new file 'info_filename', and stores 'Time', 'Ticker', 'latestPrice', 'latestVolume', 'Close', 'Open', 'low', 'high' 
    in a csv form. Script will continue to append recent stock information every minute until time_lim is reached. 

#query.py:
    Run from command line with: 
    python3 query.py –verbose True/False –file info_filename –ticker ticker –time time
    
    A module function that takes the information file name,'info_filename', time, 'time' and ticker, 'ticker' as input. Query reads 
    information from a csv info file and searches for an instance of a ticker matched with a particular time. If this ticker and time
    combination if found, the file returns all the information found from the info file for this combination. When there is a verbose
    flag, the query also outputs the number of rows and columns in an info file as well as the labels for said file

#predictor.py:
    Run from command line with:
    python3 predictor.py ticker info_filename graph_filename column_name t

    A module function that takes a ticker, an information file, a graph file name, a column (latestPrice or latestVolume),
    and a time. It opens the information file and gathers all column information for the specified ticker. It then uses
    sklearn to set up a linear regression model for training. It uses the time column from the infofile as the x 
    variable and the column information as the y value. After training, the function makes stock predictions for the 
    next t minutes based on latestPrice or latestVolume. Finally, it uses matplotlib to create a line graph for the
    stock prediction. This graph contains a line plot from the historical data and a line plot for the prediction data

