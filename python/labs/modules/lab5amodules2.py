"""
Author: Yost
Title: Lab 5A Modules
Date: 12 Sep 2018
"""
def calcMenu():
    print "Hello and welcome to the calculator.  We can perform a few functions here.  Which would you like?"
    print "Choose from the selections below.  Options 1 through 6 will take 2 to 10 arguments."
    print "Type your operation and press the <Enter> key."
    choice = raw_input("1)Add\n2)Subtract\n3)Divide\n4)Multiply\n5)Exponentiate\n6)Mystery\n7)Fibonacci\n") #take input
    return choice