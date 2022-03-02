# bmi.py
# This program calculates the user's BMI from 2 inputs, height and weight
# Author: David Higgins

height = float(input("Enter your height in metres: ")) #takes an input and uses float to convert it to an decimal number, assigns value to variable called height
weight = float(input("Enter your weight in kilograms: ")) #uses same functions as line above to assign a value to variable weight

bmi = weight//height**2         #this calculates the BMI. // is used to get a decimal answer.
           
print("Your BMI is {} kg/m^2".format(bmi(height,weight)))  #prints a string that includes the value of the variable bmi