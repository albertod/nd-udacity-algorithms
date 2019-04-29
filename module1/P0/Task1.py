from Helper import *
"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

import csv

def getCallAndTextNumbers():
    response = set()
    with open('texts.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            response.add(row[0])
            response.add(row[1])

    with open('calls.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            response.add(row[0])
            response.add(row[1])

    return len(response)

def solveP1():
    numbers = getCallAndTextNumbers()
    print(f'There are {numbers} different telephone numbers in the records.')

solveP1()