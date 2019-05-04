from Helper import *

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

# Input Calls records
# Output:
1. Get areaa code and mobile prefixes called from (080)
2. Get the % of calls made from (080) to (080)

# procedure
1.get a lsit with all the records where the src_number starts with (080)
2. do a loop where we do 2 things for each record
 a. save the area code || prefix to a set (that will be sorted) prefix_codes
 b. If the dst_number's prefix is (080) save the number to a list --> banagalore_local_calls

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

import csv


def getBangaloreCalls():
    prefixes = set()
    calls_to_bangalore = list()
    calls_from_bangalore = 0
    with open('calls.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            call = Call(row[0], row[1], row[2], row[3])
            if (row[0].startswith('(080)')):  # It is a call from bangalore
                calls_from_bangalore += 1
                # check is not telemarketer
                if not call.dst_number.startswith('140'):
                    if call.dst_number.startswith("("):
                        # Landline
                        prefixes.add(call.dst_number[call.dst_number.find(
                            "(") + 1:call.dst_number.find(")")])
                    else:
                        # Mobile phone
                        prefixes.add(call.dst_number.split(" ")[0][:4])

                    if call.dst_number.startswith('(080)'):
                        calls_to_bangalore.append(call.dst_number)

    percentage_calls_to_bangalore = (
        len(calls_to_bangalore)/calls_from_bangalore) * 100

    return prefixes, percentage_calls_to_bangalore


def printPhoneCodes(codeList):
    print("The numbers called by people in Bangalore have codes:")
    codeList = sorted(codeList)
    for code in codeList:
        print(code)


def solveP3():
    prefixes, calls_percentage = getBangaloreCalls()

    # Print response
    printPhoneCodes(prefixes)
    print()
    print(f"{round(calls_percentage, 2)} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")


solveP3()
