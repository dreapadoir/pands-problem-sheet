#es.py
#program to count the number of es in a text file
#Author: David Higgins

import os                               #required for finding filepaths
import sys                              #required for taking in filename from command line

filename = sys.argv[1]                  #takes in the filename from the command line
filepaths = []                          #creates an empty list to hold filepaths

def readData():                         #defines a function to count the es in a file
    with open(filepaths[fchoice], "rt") as f:   #opens the file by taking the filepath at index that matches the value of fchoice, as text and with read privileges
        data = f.read()                         #creates a variable that stores the contents of the file
        numberOfEs = data.count("e")            #uses the count function with e as argument to count es in data and assign the result to a variable numberOfEs
        print("The number of es in the file is {}".format(numberOfEs)) #returns a string stating the number of es in the file


for root, dirs, files in os.walk("/", topdown = True):     #uses os.walk to search for filename in root and all its subdirectories
    for name in files:
        if name == filename:
            filepaths.append(os.path.abspath(os.path.join(root, name))) #when a file matching filename is found, its filepath is appended to the list filepaths


if len(filepaths) > 1:      #if more that 1 filepath is found this block runs
    index = 1               #creates a variable that will be used to assign numbers to the filepaths
    choicetruth = True      #creates a variable that will be used to manage errors in the try except block
    print("{} results found for {}:".format(len(filepaths),filename)) #prints a string saying how many filepaths were found
    for path in filepaths:  #for loop used to print out all filepaths and assign a number to each using index variable
        print(index, path)
        index += 1
    while choicetruth == True:  #used to manage errors when invalid value entered by user
        try:
            choice = input("Enter the number of the search result you want to choose: ") #asks the user to choose which filepath to use and assigns the value entered to variable choice
            fchoice = int(choice) - 1   #converts choice to int and decrements by 1 so fchoice will match list index values
            readData()                  #calls readData and counts es if all is correct
            choicetruth = False         #sets choicetruth to False and stops while loop
        except:
            print("Error: you need to enter a number between 1 and {}.".format(len(filepaths))) #if user enters invalid value at line 33, a string is printed asking them to enter a number between 1 and len(filepaths)
    
elif len(filepaths) == 1:       #if only one filepath is found, fchoice is set to 0 and readData is called
    fchoice = 0
    readData()

elif len(filepaths) == 0:       #if no filepath is found, a string is printed stating that file is not found
    print("File {} not found".format(filename))
