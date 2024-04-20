import sys
import csv
from tabulate import tabulate

def print_grid(file_name):
    try:
       
        with open(file_name,'r') as file:
            reader = csv.reader(file)
            table = tabulate(reader,headers="firstrow",tablefmt="grid")
            return table
    except FileNotFoundError:
        sys.exit("File does not exist")
        
        
def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1][-4:] != ".csv":
            sys.exit("Not a CSV file")
        else:
            print(print_grid(sys.argv[1]))
            

if __name__ == '__main__':
    main()
        