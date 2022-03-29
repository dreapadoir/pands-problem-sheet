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
The user is prompted to enter a positive integer using the input() function. The value entered is explictly declared as an integer using int() and assigned to the variable number. A variable index is intialised as 0. This variable will be used to track the number of iterations required to converge to 1. A list called collatzlist is initialised with the current value of number (the number entered by the user).

A while loop is initiated with the condition that number is not equal to 1. Within the while loop is an if statement that runs one of two blocks of code depending on whether the current value of number is odd or even.

On completion of this calculation, the variable number is updated with the new value. The value of index is incremented by 1. The append function is used to add the current value of number to the collatzlist.

When number is equal to 1, the while loop terminates and a string is printed stating the sequence has converged to 1 and how many iterations it took to converge. The collatzlist is printed showing the sequence from the initial value the user entered to when it converged to one.

### References
[Collatz Conjecture - Wikipedia](https://en.wikipedia.org/wiki/Collatz_conjecture)

## Week 5 problem
Create a program that returns whether today is a weekday or the weekend.

## Week 5 solution
[weekday.py](weekday.py)

I used the strftime method from the datetime module to assign the actual weekday to the variable day. Since the days of the week don't change, a tuple is a suitable structure to use. I created two tuples, one for weekdays and one for the weekend. 

Using an if statement I checked if the value of day is in the weekday tuple first. If it is, a string is printed stating what day it is and that it is a weekday. If the if statement is false, an elif statements checks if the value of day is in the tuple weekend. By default, it should be since the days of the week are a finite set. It prints a string saying what day it is and that it is the weekend.

### References
(https://www.delftstack.com/howto/python/python-datetime-day-of-week/)

## Week 6 problem
Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.

## Week 6 solution
I used Newton's method to approximate a square root for this task. Newton's method requires a number and a tolerance. I created two variables, varN and varTol, to hold these values and explicitly declared them as floats. varX is created and set to varN as the first guess.

This method involves carrying out the calculation root = 0.5 * (X + (N / X)), where N is the number for which the square root is being sought and X is the current guess of the root. Initially X is set to N. I defined a function, sqrt(), that carries out this calculation. 

varRoot is defined as the value returned by sqrt() with varN and varX passed in as arguments. varRoot then becomes the current guess of the square root. A while loop then compares the difference between varRoot and varX and the value of varTol. If the difference between the current guess (varRoot) and the previous guess (varX) is greater than the tolerance (varTol), the program sets varX equal to varRoot and calls sqrt() again. This will run until the difference between the guesses is less than the tolerance.

When the while loop completes, a print statement shows the original number and its approximated square root.

### References
(https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/#:~:text=Let%20N%20be%20any%20number,correct%20square%20root%20of%20N.)

## Week 7 problem

## Week 7 solution

### References

## Week 8 problem

## Week 8 solution

### References
(https://stackoverflow.com/questions/5283649/plot-smooth-line-with-pyplot)
