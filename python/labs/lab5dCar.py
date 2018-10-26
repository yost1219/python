"""
Author: Yost
Title: Lab5d Car
Date: 17 Sep 2018
"""

class Car():
#set defaults
    name=None

    def __init__(self,make,model):
        self.make=make
        self.model=model

#setters/getters
    def setMake(make):
        self.make=make
    def getMake(self):
        return self.make
    def setModel(model):
        self.model=model
    def getModel(self):
        return self.model