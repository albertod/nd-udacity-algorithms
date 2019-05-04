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
    calls_time = {}
    with open('calls.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            call = Call(row[0], row[1], row[2], row[3])
            # Add time to src_call_number
            calls_time[str(call.src_number)] = calls_time.get(
                str(call.src_number), 0) + int(call.time)
            # Add time to dst_call_number
            calls_time[str(call.dst_number)] = calls_time.get(
                str(call.dst_number), 0) + int(call.time)

    return calls_time


def solveP2():
    calls = getCalls()
    longest_call = max(calls, key=calls.get)
    print(
        f'{longest_call} spent the longest time,{calls[longest_call]} seconds, on the phone during September 2016.'
    )


solveP2()
