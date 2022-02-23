#program to approximate a square root of any positive real number using Newton's method
#Author: David Higgins

varN = float(input("Enter number: "))
varTol = float(input("Enter tolerance: "))
varX = varN

def newton(N, X):
    return 0.5 * (X +(N/X))

varRoot = newton(varN, varX)

while abs(varRoot - varX) > varTol:
    varX = varRoot
    varRoot = newton(varN, varX)

print("The square root of", varN," is approximately", varRoot)