"""
Author: Yost
Title: Lab 5A
Date: 12 Sep 2018

Lab 5A: Utilizing Modules and Packages
Instructions

Using your calculator you created from Lab4A, split up the functionality into modules and utilize packaging. Some things you could split up:

    The user menu into it's own module on a higher level package
    Opeations into one module, lower level
    Algorithms into one module, lower level
    etc

Requirments

    All requirments from Lab4A
    Utilize clean and proper dir and module names

"""

from modules.lab5amodules2 import *
from lab5amodules import *

#main
def calculator():
    calcMenu()

#addition
    if choice == '1': 
        add()
#subtraction
    elif choice == '2': 
        subtract()
#division
    elif choice == '3': 
        divide()
#multiplication
    elif choice == '4': 
        multiply()
#power
    elif choice == '5': 
        exponentiate()
#mystery
    elif choice == '6': 
        mystery()
#fibonacci
    elif choice == '7': 
        fibonacci()
#else
    else:
        print "That is not a valid option.  Goodbye."
        return

calculator()