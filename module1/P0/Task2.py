from Helper import *
"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
import csv


def getCalls():
    calls = []
    with open('calls.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            calls.append(Call(row[0], row[1], row[2], row[3]))

    return calls


def solveP2():
    calls = getCalls()
    longest_call = max(calls, key=lambda call: int(call.time))
    print(f'{longest_call.src_number} spent the longest time, {longest_call.time} seconds, on the phone during September 2016.')


solveP2()
