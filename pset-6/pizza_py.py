import csv
import sys
from tabulate import tabulate

def main():
    table = []
    
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    else:
        try:
            with open(sys.argv[1], "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    table.append(row)
                
        except FileNotFoundError:
            sys.exit("File does not exist")
    
    print(tabulate(table[1:], table[0], tablefmt="grid"))
main()