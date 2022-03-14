#plottasks.py
#program to plot the functions x, x^2 and x^3
#Author: David Higgins

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

xpoints = np.array(range(0,5))  #creates variable that holds the domain of the functions f, g and h

f = xpoints                     #creates f(x) = x
g = xpoints ** 2                #creates g(x) = x^2
h = xpoints ** 3                #creates h(x) = x^3

names = ['$f(x) = x$','$gx) = x^{2}$', '$h(x) = x^{3}$'] #list of the functions names in TeX

def xtickrange(tickmax):                #defines a function that returns a list of values at 0.5 unit intervals up to the max of a range
    domain = range(0,tickmax)
    ticklist = [0]
    while max(ticklist) < max(domain):
        ticklist.append(max(ticklist) + 0.5)

xnew = np.linspace(0, 4, num=40, endpoint=True)
hcubic = interp1d(xpoints, g, kind='cubic')
gcubic = interp1d(xpoints, h, kind='cubic')

plt.plot(xpoints, f, 'bo-')            #this block of code plots each of the 3 functions on the same graph over the domain defined in xpoints
plt.plot(xnew, gcubic(xnew), 'r--', label='cubic')
plt.plot(xnew, hcubic(xnew), 'y--', label='cubic')
plt.title('Week 08 task: plottasks.py') #adds a title to the plot
plt.legend(names)               #creates a legend using the names of the functions typeset in TeX
plt.xlabel('x values')          #these two lines add labels to the x and y axis
plt.ylabel('y values')
plt.minorticks_on()             #makes the minor ticks visible
plt.grid()                      #adds a grid to the plot
plt.xticks(xtickrange(4))       #uses the xtickrange function to add labels at 0.5 unit intervals to x axis
plt.show()                      #this line shows the visualisation