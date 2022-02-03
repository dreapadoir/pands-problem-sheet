#secondstring.py
#program to print only every second letter of a string in reverse
#Author: David Higgins

txt = input('Enter a sentence: ')       #input function takes in a sentence as a string
length = len(txt)                       #this creates a variable with the number of characters in the variable txt

sl = slice(length, 0, -2)               #sl sets the slice function to start at the position of the last character (length) and stop at position 0. setting the last argument to -2 makes it run in reverse and leave out every 2nd character
print(txt[sl])                          #this sets txt to be sliced by sl and the result returned printed