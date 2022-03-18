#es.py
#program to count the number of es in a text file
#Author: David Higgins

import os
import sys

filename = sys.argv[1]
filepaths = []

def readData():
    with open(filepaths[fchoice], "rt") as f:
        data = f.read()
        numberOfEs = data.count("e")
        print("The number of es in the file is {}".format(numberOfEs))


for root, dirs, files in os.walk("/home/", topdown = True):
    for name in files:
        if name == filename:
            filepaths.append(os.path.abspath(os.path.join(root, name)))


if len(filepaths) > 1:
    index = 1
    choicetruth = True
    print("{} results found for {}:".format(len(filepaths),filename))
    for path in filepaths:
        print(index, path)
        index += 1
    while choicetruth == True:
        try:
            choice = input("Enter the number of the search result you want to choose: ")
            fchoice = int(choice) - 1
            readData()
            choicetruth = False 
        except:
            print("Error: you need to enter a number between 1 and {}.".format(len(filepaths)))
    
elif len(filepaths) == 1:
    fchoice = 0
    readData()

elif len(filepaths) == 0:
    print("File not found")
