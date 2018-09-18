"""
Author: Yost
Title: Lab 3F FizzBuzz
Date: 10 Sep 2018

Lab 3F FizzBuzz
Instructions:

Requirments:

    Adhere to PEP8 (Comments, formatting, style, etc)
    Utilize proper formatting
    Utilize proper and clean loops and conditionals
    Follow instructions above

Additional:

    Create two versions:
        One version which is as short as possible
        Another version which is as drawn out and creative as possible

"""

"""
#create one version which is as short as possible

def fizzBuzz():
    i = 1
    while i <= 100: #loop 1 to 100
        if ((i%3==0) and (i%5==0)): #if i is divisible by 3 and 5 print FizzBuzz
            print "FizzBuzz"
        if (i%3==0): #if i is divisible by 3 print Fizz
            print "Fizz"
        elif (i%5==0): #if i is divisible by 5 print Buzz
            print "Buzz"
        else:
            print "{}".format(i) #else print the number
        i+=1

fizzBuzz()
"""

"""
#create one version which is as drawn out and creative as possible
def fizzBuzz():
    i = 1
    while i <= 100:
        if((i%2==0) and (i%3==0) and (i%5==0) and (i%7==0) and (i%11==0) and (i%13==0)):
            print "PopFizzBuzzBangCrackPow"
        elif((i%2==0) and (i%3==0) and (i%5==0) and (i%7==0) and (i%11==0)):
            print "PopFizzBuzzBangCrack"
        elif((i%2==0) and (i%3==0) and (i%5==0) and (i%7==0) and (i%13==0)):
            print "PopFizzBuzzBangPow"
        elif((i%2==0) and (i%3==0) and (i%5==0) and (i%11==0) and (i%13==0)):
            print "PopFizzBuzzCrackPow"
        elif((i%2==0) and (i%3==0) and (i%7==0) and (i%11==0) and (i%13==0)):
            print "PopFizzBangCrackPow"
        elif((i%2==0) and (i%5==0) and (i%7==0) and (i%11==0) and (i%13==0)):
            print "PopBuzzBangCrackPow"
        elif((i%3==0) and (i%5==0) and (i%7==0) and (i%11==0) and (i%13==0)):
            print "FizzBuzzBangCrackPow"
        elif((i%2==0) and (i%3==0) and (i%5==0) and (i%7==0)):
            print "PopFizzBuzzBang"
        elif((i%2==0) and (i%3==0) and (i%5==0) and (i%11==0)):
            print "PopFizzBuzzCrack"
        elif((i%2==0) and (i%3==0) and (i%5==0) and (i%13==0)):
            print "PopFizzBuzzPow"
        elif((i%2==0) and (i%3==0) and (i%7==0) and (i%11==0)):
            print "PopFizzBangCrack"
        elif((i%2==0) and (i%3==0) and (i%7==0) and (i%13==0)):
            print "PopFizzBangPow"
        elif((i%2==0) and (i%3==0) and (i%11==0) and (i%13==0)):
            print "PopFizzCrackPow"
        elif((i%2==0) and (i%5==0) and (i%7==0) and (i%11==0)):
            print "PopBuzzBangCrack"
        elif((i%2==0) and (i%5==0) and (i%7==0) and (i%13==0)):
            print "PopBuzzBangPow"
        elif((i%2==0) and (i%5==0) and (i%11==0) and (i%13==0)):
            print "PopBuzzCrackPow"
        elif((i%2==0) and (i%7==0) and (i%11==0) and (i%13==0)):
            print "PopBangCrackPow"
        elif((i%3==0) and (i%5==0) and (i%7==0) and (i%11==0)):
            print "FizzBuzzBangCrack"
        elif((i%3==0) and (i%5==0) and (i%7==0) and (i%13==0)):
            print "FizzBuzzBangPow"
        elif((i%3==0) and (i%5==0) and (i%11==0) and (i%13==0)):
            print "FizzBuzzCrackPow"
        elif((i%3==0) and (i%7==0) and (i%11==0) and (i%13==0)):
            print "FizzBangCrackPow"
        elif((i%5==0) and (i%7==0) and (i%11==0) and (i%13==0)):
            print "BuzzBangCrackPow"
        elif((i%2==0) and (i%3==0) and (i%5==0)):
            print "PopFizzBuzz"
        elif((i%2==0) and (i%3==0) and (i%7==0)):
            print "PopFizzBang"
        elif((i%2==0) and (i%3==0) and (i%11==0)):
            print "PopFizzCrack"
        elif((i%2==0) and (i%3==0) and (i%13==0)):
            print "PopFizzPow"
        elif((i%2==0) and (i%5==0) and (i%7==0)):
            print "PopBuzzBang"
        elif((i%2==0) and (i%5==0) and (i%11==0)):
            print "PopBuzzCrack"
        elif((i%2==0) and (i%5==0) and (i%13==0)):
            print "PopBuzzPow"
        elif((i%2==0) and (i%7==0) and (i%11==0)):
            print "PopBangPow"
        elif((i%2==0) and (i%7==0) and (i%13==0)):
            print "PopBangPow"
        elif((i%2==0) and (i%11==0) and (i%13==0)):
            print "PopCrackPow"
        elif((i%3==0) and (i%5==0) and (i%7==0)):
            print "FizzBuzzBang"
        elif((i%3==0) and (i%5==0) and (i%11==0)):
            print "FizzBuzzCrack"
        elif((i%3==0) and (i%5==0) and (i%13==0)):
            print "FizzBuzzPow"
        elif((i%3==0) and (i%7==0) and (i%11==0)):
            print "FizzBangCrack"
        elif((i%3==0) and (i%7==0) and (i%13==0)):
            print "FizzBangPow"
        elif((i%3==0) and (i%11==0) and (i%13==0)):
            print "FizzCrackPow"
        elif((i%5==0) and (i%7==0) and (i%11==0)):
            print "BuzzBangCrack"
        elif((i%5==0) and (i%7==0) and (i%13==0)):
            print "BuzzBangPow"
        elif((i%5==0) and (i%11==0) and (i%13==0)):
            print "BuzzCrackPow"
        elif((i%7==0) and (i%11==0) and (i%13==0)):
            print "BangCrackPow"
        elif((i%2==0) and (i%3==0)):
            print "PopFizz"
        elif((i%2==0) and (i%5==0)):
            print "PopBuzz"
        elif((i%2==0) and (i%7==0)):
            print "PopBang"
        elif((i%2==0) and (i%11==0)):
            print "PopCrack"
        elif((i%2==0) and (i%13==0)):
            print "PopPow"
        elif((i%3==0) and (i%5==0)):
            print "FizzBuzz"
        elif((i%3==0) and (i%7==0)):
            print "FizzBang"
        elif((i%3==0) and (i%11==0)):
            print "FizzCrack"
        elif((i%3==0) and (i%13==0)):
            print "FizzPow"
        elif((i%5==0) and (i%7==0)):
            print "BuzzBang"
        elif((i%5==0) and (i%11==0)):
            print "BuzzCrack"
        elif((i%5==0) and (i%13==0)):
            print "BuzzPow"
        elif((i%7==0) and (i%11==0)):
            print "BangCrack"
        elif((i%7==0) and (i%13==0)):
            print "BangPow"
        elif((i%11==0) and (i%13==0)):
            print "CrackPow"
        elif(i%2==0):
            print "Pop"
        elif(i%3==0):
            print "Fizz"
        elif(i%5==0):
            print "Buzz"
        elif(i%7==0):
            print "Bang"
        elif(i%11==0):
            print "Crack"
        elif(i%13==0):
            print "Pow"
        else:
            print "{}".format(i)
        i+=1

fizzBuzz()
"""

""""
def fizzBuzz():
    f = "Fizz"
    b = "Buzz"
    i = 1
    while i<=100:
        fizz = f*(i%3 == 0)
        buzz = b*(i%5 == 0)
        print "{}: {}".format(i, fizz + buzz)
        i+=1

fizzBuzz()
"""


def fizzBuzz():
    i = 1
    p1 = "Pop"
    f = "Fizz"
    b1 = "Buzz"
    b2 = "Bang"
    c = "Crack"
    p2 = "Pow"
    while i<=100: #all 6 show up at i = 30030
        pop = p1*(i%2==0)
        fizz = f*(i%3==0)
        buzz = b1*(i%5==0)
        bang = b2*(i%7==0)
        crack = c*(i%11==0)
        pow = p2*(i%13==0)
        print "{}: {}".format(i, pop+fizz+buzz+bang+crack+pow)
        i+=1

fizzBuzz()