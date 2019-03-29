import sys
import csv
import argparse

#EXAMPLE OF HOW TO RUN
#python3 query.py True test.csv AAPL 00:00 

#sys.argv[1] = Verbose T/F
#sys.argv[2] = csv file name
#sys.argv[3] = ticker symbol
#sys.argv[4] = time

#stores the column names
fields = []

#creates a dictionary to support hashing and get faster returns
company = {}

#keeps track of number of rows
numrows = 0

def read_csv_file(filename):
    """
    Opens a csv file and reads its data
    Stores all the column names in a list called fields
    Creates a dictionary where the keys are the symbol names
    and each row of values associated with said symbol
    are appended as a list of values
    This allows multiple rows to be assigned to the same
    key/symbol
    """
    global numrows
    with open(filename,'r') as csvfile:
        csvreader = csv.reader(csvfile)

        #Gets the field names (first row) and stores them
        for row in csvreader:
            fields.append(row)
            break

        #Gets and stores data from the following rows
        for row in csvreader:
            if row[1] not in company:
                company.setdefault(row[1],[]) .append(row)
            elif row[1] in company:
                company[row[1]].append(row)
            numrows+=1

def find_symbol(ticker, verbose, time):
    """
    Indexes into the dictionary based on the symbols name stored in sys.argv[3]
    Searches the rows associated with the symbol to find the time specified
    If verbose is set to true, output the number of rows, columns, and all the
    field names
    """
    if ticker in company:
        for i in range(len(company[ticker])):
            if company[ticker][i][0] == time:
                for val in range(len(fields[0])):
                    print(f"{fields[0][val]}: {company[ticker][i][val]}")
                break

    if verbose:
        print(f"Number of rows: {numrows} (not counting row of labels)")
        print(f"Number of columns: {len(fields[0])}")
        print(' '.join(field for field in fields[0]))


def parse_args(args):
    """ Configure parsing of command line arguments """
    parser = argparse.ArgumentParser(description=(f"Prints details corresponding to ticker"
        " and specific time"))
    parser.add_argument("-verbose", "-v", nargs='?', default=None, type=bool, 
        help="when True, the number of rows and number of columns in the information"
        " file will be printed out as well as the names of the columns.")
   
    parser.add_argument("-file", nargs='?', default=None, type=str, 
        help="information filename")
    parser.add_argument("-ticker", nargs='?', default=None, type=str, 
        help="ticker name")
    parser.add_argument("-time", nargs='?', default=None, type=str, 
        help="requested time")

    args = parser.parse_args(args)
    return args    


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    verbose = args.verbose
    info_file = args.info_filename
    ticker = args.ticker
    time = args.time
   
    read_csv_file(info_file)
    find_symbol(ticker, verbose, time)
    
   


