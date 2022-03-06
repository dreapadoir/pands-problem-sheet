#es.py
#program to count the number of es in a text file
#Author: David Higgins

import os
import sys

filename = sys.argv[1]
filepaths = []

def readData():
    if len(filepaths) >= 1:
        with open(filepaths[choice], "rt") as f:
            data = f.read()
            print(data.count("e"))
    else:
        print("File not found")

for root, dirs, files in os.walk("/home/", topdown = True):
   for name in files:
        if name == filename:
            filepaths.append(os.path.abspath(os.path.join(root, name)))

if len(filepaths) > 1:
    index = 1
    print("{} results found for {}:".format(len(filepaths),filename))
    for path in filepaths:
        print(index, path)
        index += 1
    choice = int(input("Enter the number of the search result you want to choose: ")) -1
    while choice > len(filepaths) or choice < 0:
        choice = int(input("Please enter a number between 1 and {}: ".format(len(filepaths))))
elif len(filepaths) <= 1:
    choice = 0

dataset = readData()
