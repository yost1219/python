"""
Author: Yost
Title: Lab5C Person
Date: 17 Sep 2018
"""

class Person():
#set defaults
    name=None
    age=None
    gender=None

    def __init__(self,name):
        self.name=name

#setters
    def setName(self,name):
        self.name=name
    def setAge(self,age):
        self.age=age
    def setGender(self,gender):
        self.gender=gender
		
#getters
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getGender(self):
        return self.gender

