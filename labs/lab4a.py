"""
Author: Yost
Title: Lab 4A
Date: 10 Sep 2018

Lab 4A: Calculator

Instructions

Create a fully functional calculator using BOTH functions and lambdas. 
Create a user menu as well as a "screen" where the numbers and operations 
take place. The calculator needs to have the following functionality:

    Addition
    Subtraction
    Division
    Multiplication
    Power
    At least two math algorithms (One can be your Fibonacci)

Requirements

    Adhere to PEP8
    Functionality requirements above
    Utilize user input and proper validation
    Utilize proper formatting
    Utilize proper and clean statements and loop

Additional

    More than two numbers
    Continuous operations (5 + 5 + 2 - 1 / 2 for example)
    Additional operations
    Additional math algorithms
    etc
"""

def calculator():
    print "Hello and welcome to the calculator.  We can perform a few functions here.  Which would you like?"
    print "Choose from the selections below.  Options 1 through 6 will take 2 to 10 arguments."
    print "Type your operation and press the <Enter> key."
    choice = raw_input("1)Add\n2)Subtract\n3)Divide\n4)Multiply\n5)Exponentiate\n6)Mystery\n7)Fibonacci\n") #take input
#addition
    if choice == '1': 
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
    elif choice == '2': 
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
    elif choice == '3': 
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
    elif choice == '4': 
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
    elif choice == '5': 
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
    elif choice == '6': 
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
    elif choice == '7': 
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
    else:
        print "That is not a valid option.  Goodbye."
        return

calculator()