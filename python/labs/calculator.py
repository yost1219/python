
"""
Author: ELF
Course: Python
version: Python 3.X
FileName: lab4a.py
Lab 4a: Calculator
Recommended Version: Python 3.X
IMPORTANT: You must double click the application in windows or
download the Tkinter package in linux. The package is not
installed by default in linux but is in Windows!
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
Requirments
    Adhere to PEP8
    Functionality requirments above
    Utilize user input and proper validation
    Utilize proper formatting
    Utilize proper and clean statements and loop
Additional
    More than two numbers
    Continuous operations (5 + 5 + 2 - 1 / 2 for example)
    Additional operations
    Additonal math algorithms
    etc
"""
from Tkinter import *
from math import sqrt
#The expression variable a string of the entire equation when the user presses 
#buttons on the calculator it is used by all functions.
expression = ""                         


def press(num):
    """This is the function that adds all of the button 
    presses to the text box of the calculator.
    """ 
    global expression 
    expression = expression + str(num)
    #Once we add the new button press entry to the expression 
    #add it to the equation string var. 
    equation.set(expression) 
  
def equals():
    """Handles the math for the equation when the user presses 
    equals
    """ 
    #The try except here catches if the user inputs anything that
    #wouldn't make sense IE putting letters in
    try: 
        global expression 
        total = str(eval(expression)) 
        equation.set(total) 
        expression = ""
    except: 
        equation.set(" error ") 
        expression = "" 
  
def clear(): 
    """Clears the StringVar equation as well as the global 
    string expression
    """
    global expression 
    expression = "" 
    equation.set("0")

def fibIt():
    """Calculates the fibonacci number up the the digit in the 
    entry field
    """
    global expression
    #Check to see if there is any special characters (math signs).
    if expression.isdigit() == True:
        #Pull out the integer and store in n.
        n = int(expression)
        #Since fibonacci starts slowing down after 35, I have decided 
        # to limit it to 35 iterations.
        if n < 35:
            currentFib = 1
            lastFib = 0
            for i in xrange(n):
                temp = currentFib + lastFib
                lastFib = currentFib
                currentFib = temp
            expression = str(currentFib)
            equation.set(expression)
        else:
            equation.set(" error too large ")
    else:
        equation.set(" error invalid number")

def square_root():
    """Calculates the square root of the number in the entry field."""
    global expression
    #Check to make sure we don't have any special characters.
    if expression.isdigit() == True:
        n = int(expression)
        #Cannot sqrt negative numbers.
        if n > 0:
            #calculate the square root and store it in the expression.
            result = sqrt(n)
            expression = str(result)
            equation.set(expression)
        else:
            equation.set(" error number must be positive")
    else:
        equation.set(" error input must only be a positive integer")


#First thing is to create an instance of a Tkinter class
top = Tk()
#Title Bar text.
top.title("Calculator")
#The StringVar equation is what is shown and edited in the Entry field
equation = StringVar()
equation.set("0")
#Create the grid for the GUI so it can be resized.
Grid.rowconfigure(top, 0, weight=1)
Grid.columnconfigure(top, 0, weight=1)
#Create a frame of the GUI so we can resize it.
frame=Frame(top)
frame.grid(row=0, column=0, sticky=N+S+E+W)
#This is the text field at the top of the calculator.
Entry(frame, exportselection=0, textvariable=equation).grid(
    row=0,column=0, columnspan=6, pady=3, sticky=N+S+E+W)
#The following commands are the Buttons on the calculator.
Button(frame, text="C", command=clear).grid(row=1, column=0,
        sticky=N+S+E+W)
Button(frame, text="/", command=lambda: press("/")).grid(
        row=1, column=1, sticky=N+S+E+W)
Button(frame, text="*", command=lambda: press("*")).grid(
        row=1, column=2, sticky=N+S+E+W)
Button(frame, text="-", command=lambda: press("-")).grid(
        row=1, column=3, sticky=N+S+E+W)
Button(frame, text="7", command=lambda: press(7)).grid(
        row=2, column=0, sticky=N+S+E+W)
Button(frame, text="8", command=lambda: press(8)).grid(
        row=2, column=1, sticky=N+S+E+W)
Button(frame, text="9", command=lambda: press(9)).grid(
        row=2, column=2, sticky=N+S+E+W)
Button(frame, text="6", command=lambda: press(6)).grid(
        row=3, column=2, sticky=N+S+E+W)
Button(frame, text="5", command=lambda: press(5)).grid(
        row=3, column=1, sticky=N+S+E+W)
Button(frame, text="4", command=lambda: press(4)).grid(
        row=3, column=0, sticky=N+S+E+W)
Button(frame, text="3", command=lambda: press(3)).grid(
        row=4, column=2, sticky=N+S+E+W)
Button(frame, text="2", command=lambda: press(2)).grid(
        row=4, column=1, sticky=N+S+E+W)
Button(frame, text="1", command=lambda: press(1)).grid(
        row=4, column=0, sticky=N+S+E+W)
Button(frame, text="x^2", command=lambda: press("**")).grid(
        row=5, column=0, sticky=N+S+E+W)
Button(frame, text="0", command=lambda: press(0)).grid(
        row=5, column=1, sticky=N+S+E+W)
Button(frame, text="+", command=lambda: press("+")).grid(
        row=2, column=3, sticky=N+S+E+W)
Button(frame, text="=", command=equals).grid(
        row=3, column=3, sticky=N+S+E+W)
Button(frame, text="fib", command=fibIt).grid(
        row=5, column=3, sticky=N+S+E+W)
Button(frame, text="sqrt", command=square_root).grid(
        row=4, column=3, sticky=N+S+E+W)
Button(frame, text=".", command=lambda: press(".")).grid(
        row=5, column=2, sticky=N+S+E+W)
Button(frame, text="(", command=lambda: press("(")).grid(
        row=6, column=0, sticky=N+S+E+W)
Button(frame, text=")", command=lambda: press(")")).grid(
        row=6, column=1, sticky=N+S+E+W)
Button(frame, text="MOD", command=lambda: press("%")).grid(
        row=6, column=2, sticky=N+S+E+W)

#Loops through all the rows and columns and resizes them if the
#window is resized.
for x in range(7):
    Grid.rowconfigure(frame, x, weight=1)
for y in range(4):
    Grid.columnconfigure(frame, y, weight=1)

#Loops the application until the user closes the program.
top.mainloop()
"""



from tkinter import * #import all methods from the tkinter module


#click functions
def click():
    entered_text=textentry.get() #collects text from the text entry box below
    output.delete(0.0, END) #starts top left, ends at END
    try:
        definition = my_compdictionary[entered_text]
    except:
        definition = "Definition does not exist here."
    output.insert(END, definition)

def click0():
def click1():
def click2():
def click3():
def click4():
def click5():
def click6():
def click7():
def click8():
def click9():
def clickDecimal():
def clickPlus():
def clickMinus():
def clickDivide():
def clickMultiply():
def clickFactorial():
def clickExponent():
def clickAND():
def clickOR():
def clickXOR():

#main:
window = Tk()
window.title("Doge Calculator")
window.configure(background = "yellow") #sets background color


#my photo
photo1 = PhotoImage(file="pic.gif")
Label (window, image=photo1, bg="yellow") .grid(row=0, column=0, columnspan=5, sticky=E) #E is east (right side)


#create label
#Label (window, text= "Enter word:", bg="black", fg="white", font="none 12 bold") .grid(row=1, column=0, sticky=W) #bg is background, fg is font color, font is font type/font size/style



#create text entry box
#textentry = Entry(window, width=20, bg="white") #you can type into this box
#textentry.grid(row=2, column=0, sticky=W) #position of the text box

displayBox = Entry(window, width=56, bg="white").grid(row=2, column=0, columnspan=5, sticky=W)


#add buttons
Button(window, text="7", width=8, command=click7).grid(row=3,column=0,sticky=W)
Button(window, text="8", width=8, command=click8).grid(row=3,column=1,sticky=W)
Button(window, text="9", width=8, command=click9).grid(row=3,column=2,sticky=W)
Button(window, text="-", width=8, command=clickMinus).grid(row=3,column=3,sticky=W)
Button(window, text="+", width=8, command=clickPlus).grid(row=3,column=4,sticky=W)
Button(window, text="4", width=8, command=click4).grid(row=4,column=0,sticky=W)
Button(window, text="5", width=8, command=click5).grid(row=4,column=1,sticky=W)
Button(window, text="6", width=8, command=click6).grid(row=4,column=2,sticky=W)
Button(window, text="/", width=8, command=clickDivide).grid(row=4,column=3,sticky=W)
Button(window, text="*", width=8, command=clickMultiply).grid(row=4,column=4,sticky=W)
Button(window, text="1", width=8, command=click1).grid(row=5,column=0,sticky=W)
Button(window, text="2", width=8, command=click2).grid(row=5,column=1,sticky=W)
Button(window, text="3", width=8, command=click3).grid(row=5,column=2,sticky=W)
Button(window, text="^", width=8, command=clickExponent).grid(row=5,column=3,sticky=W)
Button(window, text="!", width=8, command=clickFactorial).grid(row=5,column=4,sticky=W)
Button(window, text="0", width=8, command=click0).grid(row=6,column=0,sticky=W)
Button(window, text=".", width=8, command=clickDecimal).grid(row=6,column=1,sticky=W)
Button(window, text="AND", width=8, command=clickAND).grid(row=6,column=2,sticky=W)
Button(window, text="OR", width=8, command=clickOR).grid(row=6,column=3,sticky=W)
Button(window, text="XOR", width=8, command=clickXOR).grid(row=6,column=4,sticky=W)



#add submit button
#Button(window, text="SUBMIT", width=6, command=click).grid(row=7, column=0, sticky=W) #click function defined above
Button(window, text="ENTER", width=15, command=clickEnter).grid(row=7, column=0, columnspan=2, sticky=W)
#clear button
Button(window, text="CLEAR", width=15, command=clickClear).grid(row=7, column=2, columnspan=2, sticky=W)

#create another level
#Label(window, text="\nDefinition:", bg="black", fg="white", font="none 12 bold") .grid(row=10, column=0, sticky=W)



#create text box
#output = Text(window, width=75, height=6, wrap=WORD, background="white")
#output.grid(row=8, column=0, columnspan=5, sticky=W)

#dictionary
my_compdictionary = {'1':'face', '2':'off'}

#exit function
def close_window():
    window.destroy()
    exit()

#exit label and button
#Label (window, text="click to exit:", bg="blue", fg="red", font="none 12 bold") .grid(row=9, column=0, stick=E)
#Button (window, text="EXIT", width=14, command=close_window).grid(row=9, column=0, sticky=W)




#run the main loop


window.mainloop()