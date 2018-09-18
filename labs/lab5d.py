"""
Author: Yost
Title: Lab 5D - Classes
Date: 14 Sep 2018

Lab 5D: Programming Classes with Composition

Note

    Remember, composition is a has a relationship vs a is a relationship. A what it can do vs what it is.
        A dog can eat
        A dog can poop
        A dog can run
        A cat can eat
        A cat can poop
        A cat can run
        A dog can bark
        A cat can meow
        OR
        A pickup truck has 2 axles
        A semi-truck has 3 axles
        A van has third row seating
        A sedan has two row seating

Instructions

    Create some vehicle types (start with just a few), pickup truck, semi truck, sedan, sports car, exotic, van, crossover, SUV, etc
        Compose the vehicles of other classes (get creative here, think of things some vehicles have that others don't):
            axles
            seating
            engines
            transmission
            Towing capacity
            Sport ability
            etc
    Create instances of different types of vehicles, ex:
        pickup truck: Ford F150, Chevy Siverado, etc
        semi truck: International, Peterbilt, Volvo
        sedan: Toyota Corolla, Honda Civic
        etc
    Do these steps last (may take a long time):
        Allow users to create the cars, selecting from a menu of selections to narrow down what type of class to make.
        Save the user vehicles into a file and allow the users to view, delete, add or modify them

Requirments

    Adhere to PEP8 and utilize proper and efficient code
    Input Validation
    Comments
    File usage
    Packages/user modules
    Proper User Class OOP Principles

Additional:

    Convert it to a racing game
	
"""

#classes for types of vehicles

#high-performance street cars
class Street():
    def __init__(self,type,make,model,drivetrain,power,weight):
        self.type=type
        self.make=make
        self.model=model
        self.drivetrain=drivetrain
        self.power=power
        self.weight=weight
		
    def stats(self):
        print "{} {} is a {} car.".format(self.make,self.model,self.type)
        print "Its drivetrain is {}.".format(self.drivetrain)
        print "It has stock {} HP.".format(self.power)
        print "Its stock weight is {}.".format(self.weight)

#rally cars
class Rally():
    def __init__(self,type,make,model,drivetrain,power,weight):
        self.type=type
        self.make=make
        self.model=model
        self.drivetrain=drivetrain
        self.power=power
        self.weight=weight
		
    def stats(self):
        print "{} {} is a {} car.".format(self.make,self.model,self.type)
        print "Its drivetrain is {}.".format(self.drivetrain)
        print "It has stock {} HP.".format(self.power)
        print "Its stock weight is {}.".format(self.weight)

#hot hatch
class Hatch():
    def __init__(self,type,make,model,drivetrain,power,weight):
        self.type=type
        self.make=make
        self.model=model
        self.drivetrain=drivetrain
        self.power=power
        self.weight=weight
		
    def stats(self):
        print "{} {} is a {} car.".format(self.make,self.model,self.type)
        print "Its drivetrain is {}.".format(self.drivetrain)
        print "It has stock {} HP.".format(self.power)
        print "Its stock weight is {}.".format(self.weight)

#classics
class Classic():
    def __init__(self,type,make,model,drivetrain,power,weight):
        self.type=type
        self.make=make
        self.model=model
        self.drivetrain=drivetrain
        self.power=power
        self.weight=weight
		
    def stats(self):
        print "{} {} is a {} car.".format(self.make,self.model,self.type)
        print "Its drivetrain is {}.".format(self.drivetrain)
        print "It has stock {} HP.".format(self.power)
        print "Its stock weight is {}.".format(self.weight)
		
#set some instances

zonda=Street("street","Pagani","Zonda C-12","MR",450,2822)
delta=Rally("rally","Lancia","Delta HF Integrale","AWD",295,2464)
turbo5=Hatch("hatchback","Renault","Turbo 5","MR",158,2138)
belair=Classic("classic","Chevrolet","Bel Air","FR",92,3345)

#print stats
#zonda.stats()
#delta.stats()
#turbo5.stats()
#belair.stats()

#user menu
choice=raw_input("Would you like to:\n1)View List\n2)Add to List\
\n3)Exit\n")
if choice=='1': #view list
    zonda.stats()
    delta.stats()
    turbo5.stats()
    belair.stats()
elif choice=='2': #add to list
    choice1=raw_input("Would you like to add:\n1)Street\n2)Rally\
    \n3)Hatchback\n4)Classic\n5)Exit\n")
    if choice1=='1': #add street
        make1=raw_input("What is the make of the car you want to add?\n")
        model1=raw_input("What is the model?\n")
        drivetrain1=raw_input("What is the drivetrain?\n")
        power1=raw_input("What is the base horsepower?\n")
        power1=int(power1)
        weight1=raw_input("What is the base weight in lbs?\n")
        weight1=int(weight1)
        model1=Street("street",make1,model1,drivetrain1,power1,weight1)
        model1.stats()
    elif choice1=='2': #add rally
        make1=raw_input("What is the make of the car you want to add?\n")
        model1=raw_input("What is the model?\n")
        drivetrain1=raw_input("What is the drivetrain?\n")
        power1=raw_input("What is the base horsepower?\n")
        power1=int(power1)
        weight1=raw_input("What is the base weight in lbs?\n")
        weight1=int(weight1)
        model1=Rally("rally",make1,model1,drivetrain1,power1,weight1)
        model1.stats()
    elif choice1=='3': #add hatchback
        make1=raw_input("What is the make of the car you want to add?\n")
        model1=raw_input("What is the model?\n")
        drivetrain1=raw_input("What is the drivetrain?\n")
        power1=raw_input("What is the base horsepower?\n")
        power1=int(power1)
        weight1=raw_input("What is the base weight in lbs?\n")
        weight1=int(weight1)
        model1=Hatch("hatchback",make1,model1,drivetrain1,power1,weight1)
        model1.stats()
    elif choice1=='4': #add classic
        make1=raw_input("What is the make of the car you want to add?\n")
        model1=raw_input("What is the model?\n")
        drivetrain1=raw_input("What is the drivetrain?\n")
        power1=raw_input("What is the base horsepower?\n")
        power1=int(power1)
        weight1=raw_input("What is the base weight in lbs?\n")
        weight1=int(weight1)
        model1=Classic("classic",make1,model1,drivetrain1,power1,weight1)
        model1.stats()
    elif choice1=='5': #exit
        print "Thank you for stopping by.  Goodbye."
    else: #invalid input
        print "Invalid choice.  Goodbye."
elif choice=='3': #exit
    print "Thank you for stopping by.  Goodbye."
else: #invalid input
    print "Invalid choice.  Goodbye."