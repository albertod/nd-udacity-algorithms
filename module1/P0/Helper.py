"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

def getCallAndText():
    calls = []
    texts = []
    with open('texts.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            texts.append(Text(row[0], row[1], row[2]))

    with open('calls.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            calls.append(Call(row[0], row[1], row[2], row[3]))

    return calls, texts

# Create class for texts
class Text:
    def __init__(self, src_number, dst_number, date):
        self.src_number = src_number
        self.dst_number = dst_number
        self.date = date

    def __str__(self):
        return f'{self.src_number} {self.dst_number} {self.date}'

# Create class for calls
class Call:
    def __init__(self, src_number, dst_number, date, time):
        self.src_number = src_number
        self.dst_number = dst_number
        self.date = date
        self.time = time

    def __str__(self):
        return f'{self.src_number} {self.dst_number} {self.date} {self.time}'
