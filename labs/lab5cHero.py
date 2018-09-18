"""
Author: Yost
Title: Lab 5C Hero
Date: 17 Sep 2018
"""

from lab5cPerson import Person

class Hero(Person):
    def __init__(self,name,heroName):
        Person.__init__(self,name)
        self.heroName=heroName
