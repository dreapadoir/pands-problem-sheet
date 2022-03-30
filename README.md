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
Write a program that reads in a text file and outputs the number of e's it contains.

## Week 7 solution
The os and sys modules are required for this code. The sys module allows a filename to be taken in from the command line as an argument. I created a variable called filename to take in the name from the user at the command line. I also initialised an empty list called filepaths to hold the paths to any files matching that filename on the users machine.

I defined a function called readData that will open the file as text and with read privileges. The contents of the file are then stored in a variable called data. Next, a variable numberOfEs is assigned the result of using count() function on data (with e passed in as an argument to count). readData then returns a string stating the number of es in the file.

readData requires the filepath to open the file using the with ...open function. The filepath is found using os.walk. This is done by specifying a starting directory, in this case the root directory, and that the search is to be carried out top down. os.walk searches for files matching the value of variable filename. If a file is found, its filepath is appended to the list filepaths.

As os.walk searches the home directory and all its subdirectories, it is possible that more than one filepath is found since files with the same name could exist in different directories. If there is more than one filepath found, an if statement is used to manage this case. A variable index is initalised as 1 to number the different filepaths. A second variable, choicetruth, is initialised to manage a try except loop.

A for loop is used to print all the filepaths in the list filepaths and assigns a number to each one. A while loop is then used to manage potential errors. The condition is that variable choicetruth is True. The try block asks the user to enter the number of the filepath they want to use. That value is taken in as the variable choice. The variable fchoice then takes the value of choice - 1, so fchoice will match the indexing of the list.

If the user enters a valid value, readData is called and choicetruth is updated to False, closing the loop. If an exception is thrown because the user enters a value outside the range 1 to len(filepaths) or type is not equal to int, the except block prints a statement telling the user to choose a number between 1 and len(filepaths). 

An elif statement sets fchoice to 0 if there is only one filepath in the list filepaths and then calls readData.

A second elif statement prints a message saying that filename is not found if there are no filepaths in the list filepaths.

### References
(https://www.tutorialspoint.com/python/python_command_line_arguments.htm)
(https://stackoverflow.com/questions/1124810/how-can-i-find-path-to-given-file)
(https://stackoverflow.com/questions/48439995/while-try-except-in-python-3)

## Week 8 problem
Write a program called plottask.py that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.

## Week 8 solution
This code requires the use of the following modules: numpy, pyplot from matplotlib and interp1d from scipy.interpolate. A numpy array called xpoints defines domain of the functions that will be used in this code. The functions are created by defining variables f, g and h which are assigned the values of xpoints, the square of xpoints and the cube of xpoints respectively.

The list names is created containing the names of the functions in TeX format. This will typeset the names and will be used in the legend.

A function called xtickrange is defined to create a list that will contain the positions of the x-axis tickmarks. xtickrange takes in an argument called tickmax that defines the upper limit of the range. A variable, domain, is assigned the value of the range from 0 to tickmax. A list called ticklist is then initialised containing the value zero. Then, a while loop appends values that increment by 0.5 to ticklist while the max value of ticklist is less than the max value of domain.

Lines 23 to 25 are code I researched that make g and h into smooth, curved lines. This code creates a series of intermediate points and plots them to approximate a smooth curve.

pyplot functions are then used to plot and show the three functions on one plot. The third argument in each of the plt.plot functions determine the colour and line style for each plot. Further plt functions add labels to the axes, a title and turn on the minorticks and grid. The plt.xticks function calls xtickrange with 4 as the argument to create the set of x tick positions. plt.legend uses the TeX labels defined in names to add typeset names to the legend.

### References
(https://stackoverflow.com/questions/5283649/plot-smooth-line-with-pyplot)
