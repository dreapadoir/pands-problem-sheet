#secondstring.py
#program to print only every second letter of a string in reverse
#Author: David Higgins

txt = input('Enter a sentence: ')       #input function takes in a sentence as a string

print(txt[::-2])                          #this uses the slicer statement to run in reverse (the minus sign), every 2nd letter (the number 2), for the full length of the string (the :: part of the statement) and the result returned printed