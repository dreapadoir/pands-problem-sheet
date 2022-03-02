#program to approximate a square root of any positive real number using Newton's method
#Author: David Higgins

varN = float(input("Enter number: "))       #this creates a variable that will hold the number we are trying to find the square root of. It is explicitly declared as a float
varTol = float(input("Enter tolerance: "))  #this creates a variable that will hold the tolerance, one of the inputs needed for the Newton method
varX = varN                                 #this creates a variable will be used to hold the guess of the root for each iteration

def newton(N, X):                           #defines a function that takes two arguments, N and X, and returns the value of the calculation for the Newton method
    return 0.5 * (X +(N/X))

varRoot = newton(varN, varX)                #creates a variable the holds the result of newton function using varN and varX as arguments

while abs(varRoot - varX) > varTol:         #initiates a while loop with the condition that it runs while difference between the last guess and the current approximation of the root is greater than varTol
    varX = varRoot                          #varRoot becomes the new guess, varX
    varRoot = newton(varN, varX)            #a new varRoot is calculated using newton

print("The square root of", varN," is approximately", varRoot)  #when the difference between the current guess, varX and the approximated root, varRoot is less than the tolerance
                                                                #a string is printed giving the approximation of the root of varN