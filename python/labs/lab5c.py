"""
Author: Yost
Title: Lab 5C: Update Hero Class
Date: 17 Sep 2018

Instructions

Update your hero class lab with the following additions:

    Create a generic Person class
    Create a Hero class that inherits from Person
    Refactor code where needed
    Utilize proper Encapsulation
    Include user input
    Use getters and setters

Requirments

    Adhere to PEP8 and utilize proper and efficient code
    Input validation
    Utilize a __init__()
    Ensure variables are correct type (class vs instance variables)
    Utilize methods for getters and setters
    Create an few instances of your class. Populate it with data utilzing a init and/or getters and setters
    Split your classes into seperate files and import them properly

Additional:

    Expand this program into a game or larger program. Some possible ideas:
        Hero vs Villain
        Battle Royal
        Guess that Hero
        etc
"""
"""
#create generic person class
class Person():
    def __init__(self,name,height,weight,birthdate,occupation)
        self.name=name							#regular human name
        self.height=height						#height in meters
        self.weight=weight						#weight in kilograms
        self.birthdate=birthdate				#MM/DD/YYYY
        self.occupation=occupation				#everyday job

#create hero class that inherits from person
class Hero(Person):
    def __init__(self,name,hero,cls,priPwr,nemesis)
        Person.__init__(self,name,height,weight,birthdate,occupation)
        self.hero=hero							#hero's name
        self.cls=cls							#classification: brawler, energy, magic, ability, etc.
        self.priPwr=priPwr						#hero's primary power
        self.colors=colors						#hero's colors
        self.nemesis=nemesis					#hero's nemesis

#print stats for person
def printStats():
    print "The person's name is {}.".format(self.name)
    print "Their height is {} meters.".format(self.height)
    print "Their weight is {} kilograms.".format(self.weight)
    print "Their birthdate is {}.".format(self.birthdate)
    print "Their occupation is {}.".format(self.occupation)

#print stats for hero
def printHeroStats():
    print "{} is also {}.".format(self.name,self.heroName)
    print "Their classification is {}.".format(self.cls)
    print "Their primary power is {}.".format(self.priPwr)
    print "Their nemesis is {}.".format(self.nemesis)

#create instances of Person
pp=Person("Peter Parker",1.77,76,"10/13/1995","photographer")					#Peter Parker aka Spider Man
ts=Person("Tony Stark",1.85,102,"06/22/1972","CEO of Stark Industries")			#Tony Stark aka Iron Man
bb=Person("Bruce Banner",1.76,58,"01/19/1974","Scientist")						#Bruce Banner aka The Incredible Hulk
cb=Person("Clint Barton",1.90,105,"08/30/1979","Soldier")						#Clint Barton aka Hawkeye

#create instances of Hero
sm=Hero("Peter","Spider-Man","mutate","web-slinging","Green Goblin")
im=Hero("Tony","Iron Man","tech","repulsor blasts","Crimson Dynamo")
ih=Hero("Bruce","The Hulk","brawler","strength","Abomination")
ha=Hero("Clint","Hawkeye","ability","training","Taskmaster")

#print some stuff
pp.printStats()
sm.printHeroStats()
ts.printStats()
im.printHeroStats()
bb.printStats()
ih.printHeroStats()
cb.printStats()
ha.printHeroStats()
"""
"""
#create person class
class Person:

    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def Name(self):
        return self.firstname + " " + self.lastname

#create hero class
class Hero(Person):

    def __init__(self, first, last, heroName):
        Person.__init__(self,first, last)
        self.heroName = heroName

    def HeroName(self):
        return self.Name() + ", " +  self.heroName

p1 = Person("Mary Jane", "Watson")
h1 = Hero("Peter", "Parker", "Spider-Man")

print(p1.Name())
print(h1.HeroName())
"""

from lab5cHero import Hero

#get good input
def getInput(stuff):
    while(True):
        try: #is input valid?
            userInput = str(raw_input(stuff))
            break
        except: #input not a string
            print("Invalid input.")
    return userInput

#get some info from user
heroName=getInput("What is the hero's name?\n")
name=getInput("What is their alter ego's name?\n")
age=getInput("How old is the hero?\n")
gender=getInput("What is their gender?\n")

#create/set instance based on user input
h1=Hero(name,heroName)
h1.setAge(age)
h1.setGender(gender)

print"Hero's name is {}.".format(h1.name)
print"Their alter ego is {}.".format(h1.heroName)
print"They are {} years old.".format(h1.age)
print"Sex: {}".format(h1.gender)