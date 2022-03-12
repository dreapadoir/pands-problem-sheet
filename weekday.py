#weekday.py
#program to determine if it is a weekday or the weekend
#Author: David Higgins

from datetime import datetime                       #imports the datetime module that makes a set of methods for working with dates, days etc. available to the program

weekdays = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday') #creates a tuple containing the weekdays. The set of weekdays never change so a tuple is more appropriate than a list
weekend = ('Saturday', 'Sunday')                                    #creates a tuple of the weekend days

day = datetime.today().strftime('%A')               #uses the strftime method and the argument %A to return the actual weekday as a string. This string is then assigned to the variable day

if day in weekdays:                                 #this line checks if day is a member of the tuple weekdays.
    print('Today is {}, it is a weekday'.format(day))       #this block runs if line 11 is true. Format places the value of variable day into the printed string

elif day in weekend:                                        #this block runs if line 11 is false. Works same as line 12
    print('Today is {}, it is the weekend'.format(day))     