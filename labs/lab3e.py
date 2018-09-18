"""
Author: Yost
Title: Lab 3E Fibonacci
Date: 7 Sep 2018



Performance Lab 3E: Fibonacci (Iterative vs Recursive)
Instructions:

    Write a file that prints out the first 100 numbers in the Fibonacci sequence iteratively
    Revist this lab and create a Fibonacci recursive function

Requirments:

    Adhere to PEP8 (Comments, formatting, style, etc)
    Utilize proper formatting
    Utilize proper and clean loops and conditionals
    Follow instructions above

Additional:

    Some additional things you can do are:
        Utilize functions
            Create the recursive solution before going over ch04
        Utilize some Python modules or built in functionality
        Ask user for range of numbers to calculate

		1, 1, 2, 3, 5, 8, 13, ....
		fib(1) = 1
		fib(2) = 1
		fib(n) = fib(n-1) + fib(n-2)
"""

def fibo():
    start = raw_input("Enter a number to start the Fibonacci sequence.\n")
    stop = raw_input("Enter a number less than or equal to 100 to stop the Fibonacci sequence.\n")
    start = int(start)-1
    stop = int(stop)-1
    fib = [1,1] #set fib[0] and fib[1] to 1
    i = 2
    j = start
    while i <= 100: #sets the first 100 values of the fib sequence
        fib.append(fib[i-1] + fib[i-2])
        i+=1
    while j <= stop: #only prints the fib entries that the user asks for
        print fib[j]
        j+=1
    return

fibo()