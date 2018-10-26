"""
Author: Yost
Title: Lab 3D - While Loop
Date: 7 Sep 2018

Lab 3D:
Instructions

    Write a program that prompts a user to input an integer and calculates the factorial of that number using a while loop.

Requirments

    Adhere to PEP8 (Comments, formatting, style, etc)
    Utilize userinput
    Utilize input validation
    Utilize proper formatting
    Utilize proper and clean loops and conditionals
    Follow instructions above
"""

def factor():
    number = raw_input("What positive number would you like to take the factorial of?")
    number = int(number)
    if number == 0:
        return 1
    elif number < 0:
        print "Cannot take a factorial of a negative number."
    else:
        result = 1
        count = 1
        while count <= number:
            factor*=count
            count+=1

factor()