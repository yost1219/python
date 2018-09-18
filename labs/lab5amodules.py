"""
Author: Yost
Title: Lab 5A Modules
Date: 12 Sep 2018
"""
#addition
def add():
    list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #set list of 10 each to 0
    input_list={'0'}
    i=0 #iterator
    user_input = raw_input("Enter up to 10 numbers to add, separated by spaces.  Excess numbers (more than 10) will not be utilized.\n") #take input
    input_list = user_input.split(' ') #split input into list of strings
    while i<len(input_list): #for each item of input
        list[i]=input_list[i] #set the default list equal to the input
        i+=1
    a=float(list[0]);b=float(list[1]);c=float(list[2]);d=float(list[3]);e=float(list[4]) #assign arguments to list values
    f=float(list[5]);g=float(list[6]);h=float(list[7]);i=float(list[8]);j=float(list[9])
    sum = lambda a,b,c,d,e,f,g,h,i,j: a+b+c+d+e+f+g+h+i+j
    print "The sum of the arguments is: {}".format(sum(a,b,c,d,e,f,g,h,i,j))
	
#subtraction
def subtract():
    list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #set list of 10 each to 0
    input_list={'0'}
    i=0 #iterator
    user_input = raw_input("Enter up to 10 numbers to subtract, separated by spaces.  Excess numbers (more than 10) will not be utilized.\n") #take input
    input_list = user_input.split(' ') #split input into list of strings
    while i<len(input_list): #for each item of input
        list[i]=input_list[i] #set the default list equal to the input
        i+=1
    a=float(list[0]);b=float(list[1]);c=float(list[2]);d=float(list[3]);e=float(list[4]) #assign arguments to list values
    f=float(list[5]);g=float(list[6]);h=float(list[7]);i=float(list[8]);j=float(list[9])
    sum = lambda a,b,c,d,e,f,g,h,i,j: a-b-c-d-e-f-g-h-i-j
    print "The sum of the arguments is: {}".format(sum(a,b,c,d,e,f,g,h,i,j))

#division
def divide():
    list = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1] #set list of 10 each to 1
    input_list={'0'}
    i=0 #iterator
    user_input = raw_input("Enter up to 10 numbers to divide, separated by spaces.  Excess numbers (more than 10) will not be utilized.\n") #take input
    input_list = user_input.split(' ') #split input into list of strings
    while i<len(input_list): #for each item of input
        list[i]=input_list[i] #set the default list equal to the input
        i+=1
    a=float(list[0]);b=float(list[1]);c=float(list[2]);d=float(list[3]);e=float(list[4]) #assign arguments to list values
    f=float(list[5]);g=float(list[6]);h=float(list[7]);i=float(list[8]);j=float(list[9])
    if ((b==0) or (c==0) or (d==0) or (e==0) or (f==0) or (g==0) or (h==0) or (i==0) or (j==0)): #error checking for invalid arguments
        print "Cannot divide by zero."
        return
    quotient = lambda a,b,c,d,e,f,g,h,i,j: float(a)/b/c/d/e/f/g/h/i/j
    print "The quotient of the arguments is {}".format(quotient(a,b,c,d,e,f,g,h,i,j))

#multiplication
def multiply():
    list = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1] #set list of 10 each to 1
    input_list={'0'}
    i=0 #iterator
    user_input = raw_input("Enter up to 10 numbers to multiply, separated by spaces.  Excess numbers (more than 10) will not be utilized.\n") #take input
    input_list = user_input.split(' ') #split input into list of strings
    while i<len(input_list): #for each item of input
        list[i]=input_list[i] #set the default list equal to the input
        i+=1
    a=float(list[0]);b=float(list[1]);c=float(list[2]);d=float(list[3]);e=float(list[4]) #assign arguments to list values
    f=float(list[5]);g=float(list[6]);h=float(list[7]);i=float(list[8]);j=float(list[9])
    product = lambda a,b,c,d,e,f,g,h,i,j: a*b*c*d*e*f*g*h*i*j
    print "The product of the arguments is: {}".format(product(a,b,c,d,e,f,g,h,i,j))

#power
def exponentiate():
    list = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1] #set list of 10 each to 1
    input_list={'0'}
    i=0 #iterator
    user_input = raw_input("Enter up to 10 numbers to exponentiate, separated by spaces.  Excess numbers (more than 10) will not be utilized.\n") #take input
    input_list = user_input.split(' ') #split input into list of strings
    while i<len(input_list): #for each item of input
        list[i]=input_list[i] #set the default list equal to the input
        i+=1
    a=float(list[0]);b=float(list[1]);c=float(list[2]);d=float(list[3]);e=float(list[4]) #assign arguments to list values
    f=float(list[5]);g=float(list[6]);h=float(list[7]);i=float(list[8]);j=float(list[9])
    result = lambda a,b,c,d,e,f,g,h,i,j: a**b**c**d**e**f**g**h**i**j
    print "The result of the exponentiation of the arguments is: {}".format(result(a,b,c,d,e,f,g,h,i,j))

#mystery
def mystery():
    list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #set list of 10 each to 0
    input_list={'0'}
    i=0 #iterator
    user_input = raw_input("Enter up to 10 numbers for the mystery equation, separated by spaces.  Excess numbers (more than 10) will not be utilized.\n") #take input
    input_list = user_input.split(' ') #split input into list of strings
    while i<len(input_list): #for each item of input
        list[i]=input_list[i] #set the default list equal to the input
        i+=1
    a=float(list[0]);b=float(list[1]);c=float(list[2]);d=float(list[3]);e=float(list[4]) #assign arguments to list values
    f=float(list[5]);g=float(list[6]);h=float(list[7]);i=float(list[8]);j=float(list[9])
    result = lambda a,b,c,d,e,f,g,h,i,j: ((a*b)-c**(d**e)+(3*f)*(g**2)-((h*i)**j))
    print "The result of the mystery equation is: {}".format(result(a,b,c,d,e,f,g,h,i,j))

#fibonacci
def fibonacci():
    start = raw_input("Enter a number to start the Fibonacci sequence.\n")
    stop = raw_input("Enter a number less than or equal to 100 to stop the Fibonacci sequence.\n")
    if user_input != True:
        print "No input received.  Goodbye."
        return
    if stop<start:
        print "Stop number cannot be less than start number.  Goodbye."
        return
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