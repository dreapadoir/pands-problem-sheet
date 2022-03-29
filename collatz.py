#program to replicate the 3n+1 problem - known as the Collatz Conjecture
#Author: David Higgins

number = int(input("Enter a positive number: ")) #create a variable to store the initial number which will be updated during each iteration of the while block
index = 0                                        #creates an index number to track how many iterations it takes for the sequence to converge

print("n_{} = {}".format(index,number))         #prints the value of n_0 (the number entered by the user)

while number != 1:                              #initiates a while loop - this code runs as long as number is not equal to 1
    if number % 2 == 0:                         #if statement that checks if number is odd or even
        number = number // 2                    #divides number by 2 if it is even
        index = index + 1                       #increments the index by 1
    else:                                       #next block of code runs if the block above is not true                                       
        number = (number * 3) + 1               #multiplies the number by 3 and adds one if current value of number is odd
        index = index + 1                       #increments the index by 1
    print("n_{} = {}".format(index,number))     #prints out the current iteration and value of number

if number == 1:
    print("Sequence has converged to 1 in {} iterations - program terminated".format(index)) #prints a message stating the program is terminated and how many iterations it took to converge to 1