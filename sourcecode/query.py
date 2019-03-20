import sys
import csv

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

def read_csv_file():
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
    with open(sys.argv[2],'r') as csvfile:
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

def find_symbol(verbose):
    """
    Indexes into the dictionary based on the symbols name stored in sys.argv[3]
    Searches the rows associated with the symbol to find the time specified
    If verbose is set to true, output the number of rows, columns, and all the
    field names
    """
    if sys.argv[3] in company:
        for i in range(len(company[sys.argv[3]])):
            if company[sys.argv[3]][i][0] == sys.argv[4]:
                for val in range(len(fields[0])):
                    print(f"{fields[0][val]}: {company[sys.argv[3]][i][val]}")
                break
    if verbose == "True":
        print(f"Number of rows: {numrows}")
        print(f"Number of columns: {len(fields)}")
        print(' '.join(field for field in fields[0]))

if __name__ == "__main__":
    read_csv_file()
    find_symbol(sys.argv[1])
