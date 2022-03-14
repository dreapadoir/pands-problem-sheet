#plottasks.py
#program to plot the functions x, x^2 and x^3
#Author: David Higgins

import numpy as np
import matplotlib.pyplot as plt

xpoints = np.array(range(0,5))  #creates variable that holds the domain of the functions f, g and h

f = xpoints                     #creates f(x) = x
g = xpoints ** 2                #creates g(x) = x^2
h = xpoints ** 3                #creates h(x) = x^3

names = ['$f(x) = x$','$gx) = x^{2}$', '$h(x) = x^{3}$'] #list of the functions names in TeX

def xtickrange(tickmax):
    domain = range(0,tickmax)
    ticklist = [0]
    while max(ticklist) < max(domain):
        ticklist.append(max(ticklist) + 0.5)

plt.plot(xpoints, f, 'bo-')            #this block of code plots each of the 3 functions on the same graph over the domain defined in xpoints
plt.plot(xpoints, g, 'rv--')
plt.plot(xpoints, h, 'ys-.')
plt.title('Week 08 task: plottasks.py')
plt.legend(names)               #creates a legend using the names of the functions typeset in TeX
plt.xlabel('x values')
plt.ylabel('y values')
plt.minorticks_on()
plt.grid()
plt.xticks(xtickrange(4))
plt.show()                      #this line shows the visualisation