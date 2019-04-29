from Helper import *

"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
def solveP0():
    # Get calls and text list
    calls, texts = getCallAndText()
    # Print first record of texts
    first_text = texts[0]
    print(f"First record of texts, {first_text.src_number} texts {first_text.dst_number} at time {first_text.date}")
    # Print last record of calls
    last_call = calls[-1]
    print(f"Last record of calls, {last_call.src_number} calls {last_call.dst_number} at time {last_call.date}, lasting {last_call.time} seconds")

solveP0()