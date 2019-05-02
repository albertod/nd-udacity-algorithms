from Helper import *
"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def getCallAndText():
    """
    Returns 3 dictionaries in a tuple
    1. All the numbers receiving calls
    2. All the numbers sending text messages
    3. All the numbers receiving text messages
    """
    receving_calls = {}
    sending_texts = {}
    receiving_texts = {}
    src_calls = set()
    
    with open('texts.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            sending_texts[row[0]] = True
            receiving_texts[row[1]] = True

    with open('calls.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            receving_calls[row[1]] = True
            src_calls.add(row[0])

    return receving_calls, sending_texts, receiving_texts, src_calls

def getPossibleTelemarketers(receving_calls, sending_texts, receiving_texts, src_calls):
    results = set()
    for call in src_calls:
        if call not in receving_calls and call not in sending_texts and call not in receiving_texts and not call.startswith("140"):
            results.add(call)
    return sorted(results)


def solveP4():
    print("These numbers could be telemarketers: ")
    receving_calls, sending_texts, receiving_texts, src_calls = getCallAndText()
    possible_telemarketers = getPossibleTelemarketers(receving_calls, sending_texts, receiving_texts, src_calls)
    print(possible_telemarketers)

# possible marketer
# dont send text -> no src_number on text.csv
# don't receive text -> no dst_number on text.csv
# don't receive calls -> not dst_number on calls.csv

# possible telemarketers are all the src_number from call.csv
solveP4()
