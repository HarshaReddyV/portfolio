import sys
import os.path
import csv
from tabulate import tabulate


if len(sys.argv) > 2:
    sys.exit('Too many command-line arguments')
elif len(sys.argv) == 1:
    sys.exit('Too few command-line arguments')
elif '.csv' not in sys.argv[1]:
    sys.exit('Not a CSV file')
elif os.path.isfile(sys.argv[1]) == False:
    sys.exit('File does not exist')

file = sys.argv[1]

table =[]

try:
    with open(file, 'r') as File:
        for line in File:
            line = line.rstrip()
            line = line.split(',')
            table.append(line)

except(FileNotFoundError):
    sys.exit()


header = table[0]
del table[0]

print(table)

print(tabulate(table, header, tablefmt="grid"))