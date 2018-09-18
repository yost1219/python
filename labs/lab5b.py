"""
Author: Yost
Title: Lab 5B - Classes
Date: 13 Sep 2018

Lab 5B: Your First Python Class
Instructions

Create a very simple super hero class. Some attributes you will need:

    Hero Name
    Real Name
    Power(s)
    Colors
    etc

Requirments

    Adhere to PEP8 and utilize proper and efficient code
    Utilize a __init__()
    Ensure variables are correct type (class vs instance variables)
    Utilize methods:
        Start to format your class using getters and setters
    Create an instance of your class. Populate it with data utilzing a init and/or getters and setters

Additional:

    Begin using encapsulation techniques
"""

"""
#class creation
class Superhero():
    def __init__(self):
        self.heroName="Psych Man"
        self.alterEgo="Shawn Spencer"
        self.powers=(["Pseudo-psychic Abilities","Snarky Attitude"])
        self.colors=(["Purple","Blue"])

    def message(self):
        print "{}'s alter ego is {}.".format(self.heroName,self.alterEgo)
        print "{}'s powers are: ".format(self.heroName,self.powers)
        print "{}'s colors are: ".format(self.heroName,self.colors)
        print self.getPowers

#get/set funcs
    def getName():
        return self.heroName
    def getAlterEgo():
        return self.alterEgo
    def getPowers():
        return self.powers
    def getColors():
        return self.colors
    def setName(name):
        self.heroName=name
    def setAlterEgo(name):
        self.alterEgo=name
    def removePower(power):
        self.powers.remove(power)
    def addPower(power):
        self.powers.append(power)
    def removeColor(color):
        self.colors.remove(color)
    def addColor(color):
        self.colors.append(color)
		
hero=Superhero()
print hero.message()  
"""

#class creation
class Superhero():
    def __init__(self,heroName,alterEgo,powers,colors):
        self.heroName=heroName
        self.alterEgo=alterEgo
        self.powers=powers
        self.colors=colors

    def message(self):
        print "{}'s alter ego is {}.".format(self.heroName,self.alterEgo)
        print "{}'s power is: {}.".format(self.heroName,self.powers)
        print "{}'s colors are: {}.".format(self.heroName,self.colors)

#set some heroes

bob = Superhero("Mr. Incredible","Bob Parr","Super strength","Black and blue")
helen = Superhero("Elastigirl","Helen Parr","Elastic body","Red and white")

#print messages
bob.message()
helen.message()
