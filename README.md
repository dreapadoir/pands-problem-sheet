# pands-problem-sheet
## 52167 Programming and Scripting - 2022
## G00411302 David Higgins

## Introduction
This repository will contain the commits for the weekly tasks on 52167 Programming and Scripting.

## Licence

## Prerequisites
This code was written on MS Visual Code (version 1.64.0) using Python 3.9.7. 
Running code contained in this repository will require Python 3.9.7 or higher.

The latest release of the Anaconda distribution will be sufficient (available [here](https://www.anaconda.com/products/individual)).

The following libraries will be required:
- datetime

## Week 2 problem
Write a program that calculates somebody's Body Mass Index (BMI).

## Week 2 solution
[bmi.py](bmi.py)
The program uses the input function to take in two user input values. These values are explicitly declared as floats and assigned to the variables height and weight. 

A function called bmi is defined, using height and weight as arguments. This function returns a calculated value that is equal to the user's BMI.

The print and format functions are used to print a string telling the user what their BMI is in the correct units.

### References
N/A

## Week 3 problem
Write a program that asks a user to input a string and outputs every second letter in reverse order.

## Week 3 solution
[secondstring.py](secondstring.py)
The user is prompted to enter a string using the input() function. This string is assigned to the variable txt. Using the slicer statement [::-2] the string is sliced in reverse, every 2nd character. The print function prints the result of this function for the user.

### References
[w3 schools](https://www.w3schools.com/python/python_howto_reverse_string.asp)

## Week 4 problem
Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation. At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. Have the program end if the current value is one.

## Week 4 solution
[collatz.py](collatz.py)
The user is prompted to enter a positive integer using the input() function. The value entered is explictly declared as an integer using int() and assigned to the variable number. A variable index is intialised as 0. This variable will be used to track the number of iterations required to converge to 1.

A while loop is initiated with the condition that number is not equal to 1. Within the while loop is an if statement that runs one of two blocks of code depending on whether the current value of number is odd or even.

On completion of this calculation, the variable number is updated with the new value. The value of index is incremented by 1. The print function is used to print out the current values of number and index.

When number is equal to 1, the while loop terminates and a string is printed stating the sequence has converged to 1 and how many iterations it took to converge.

### References
[Collatz Conjecture - Wikipedia](https://en.wikipedia.org/wiki/Collatz_conjecture)

## Week 5 problem
Create a program that returns whether today is a weekday or the weekend.

## Week 5 solution
[weekday.py](weekday.py)

I used the strftime method from the datetime module to assign the actual weekday to the variable day. 

### References
(https://www.delftstack.com/howto/python/python-datetime-day-of-week/)

## Week 6 problem

## Week 6 solution

### References
