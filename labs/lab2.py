Microsoft Windows [Version 10.0.17134.228]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Users\Student>py -2
Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> x,y = (545,24)
>>> binX = bin(x)
>>> binY = bin(y)
>>> print("{} is {} in binary. {} is {} in binary.".format(x,binX,y,binY)
...
...
... print(x)
  File "<stdin>", line 4
    print(x)
        ^
SyntaxError: invalid syntax
>>> print "{} is {} in binary. {} is {} in binary.".format(x, binX, y, binY)
545 is 0b1000100001 in binary. 24 is 0b11000 in binary.
>>> print "Values before modification: x: {} and y: {}".format(x,y)
Values before modification: x: 545 and y: 24
>>> x = x^4
>>> y = y^1
>>> print "Values after modification: x: {} and y: {}".format(x,y)
Values after modification: x: 549 and y: 25
>>> sum = x+y
>>> sum = hex(sum)
>>> sum
'0x23e'
>>> oct(8)
'010'
>>> int(x-y)
524
>>> oct(x*y)
'032635'
>>> bin(x/y)
'0b10101'
>>> int(x%3)
0
>>> int(y**2)
625
>>> answer1 = hex(x+y)
>>> answer2 = int(x-y)
>>> answer3 = oct(x*y)
>>> answer4 = bin(x/y)
>>> answer5 = int(x%3)
>>> answer6 = int(y**2)
>>> print "1: {}\n2: {}\n3: {}\n4: {}\n5: {}\n6: {}\n \b========================================".format(answer1, answer2, answer3, answer4, answer5, answer6)
1: 0x23e
2: 524
3: 032635
4: 0b10101
5: 0
6: 625
========================================
>>> binA = 0b0011
>>> binB = 0b1001
>>> binC = binA & binB
>>> decA = dec(binA)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'dec' is not defined
>>> decA = int(binA,2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: int() can't convert non-string with explicit base
>>> print(binA)
3
>>> decA = int(binA)
>>> decB = int(binB)
>>> binA = bin(binA)
>>> binB = bin(binB)
>>> print "Results:\n-Decimal- A: {} B: {}\n-Binary- A: {} B: {}".format(decA, decB, binA, binB)
Results:
-Decimal- A: 3 B: 9
-Binary- A: 0b11 B: 0b1001
>>> foo(x) = 1.07*x
  File "<stdin>", line 1
SyntaxError: can't assign to function call
>>> def foo(x): 1.07*x
...
>>> help(def)
  File "<stdin>", line 1
    help(def)
           ^
SyntaxError: invalid syntax
>>> help
Type help() for interactive help, or help(object) for help about object.
>>> help()

Welcome to Python 2.7!  This is the online help utility.

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at http://docs.python.org/2.7/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, or topics, type "modules",
"keywords", or "topics".  Each module also comes with a one-line summary
of what it does; to list the modules whose summaries contain a given word
such as "spam", type "modules spam".

help>

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> def taxes(x):
...     print "cost of the item with tax is: {}".format(1.07*x)
...     return
...
>>> taxes(1)
cost of the item with tax is: 1.07
>>> taxes(1.99)
cost of the item with tax is: 2.1293
>>> def taxes(x):
...     print "Cost of the item with tax is: ${}".format(1.0825*x)
...     return
...
>>> taxes(.99)
Cost of the item with tax is: $1.071675
>>> def taxes(x):
...     print "cost of the item with tax is: {}".format(1.0825*x)
...     return
...
>>> price = input(
...
...
...
...
... price = input(
...
... price = input('What is the cost of the item before tax?')
... print(input)
  File "<stdin>", line 9
    print(input)
        ^
SyntaxError: invalid syntax
>>>