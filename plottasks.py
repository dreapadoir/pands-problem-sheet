#plottasks.py
#program to plot the functions x, x^2 and x^3
#Author: David Higgins

import numpy as np
import matplotlib.pyplot as plt

xpoints = np.array(range(0,5))  #creates variable that holds the domain of the functions f, g and h

f = xpoints                     #creates f(x) = x
g = xpoints ** 2                #creates g(x) = x^2
h = xpoints ** 3                #creates h(x) = x^3

plt.plot(xpoints, f)            #this block of code plots each of the 3 functions on the same graph over the domain defined in xpoints
plt.plot(xpoints, g)
plt.plot(xpoints, h)

plt.show()                      #this line shows the visualisation