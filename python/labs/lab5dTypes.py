"""
Author: Yost
Title: Lab 5d Types
Date: 17 Sep 2018
"""

from lab5dCar import Car

#street,rally,classic,hatch
class Street(Car):
    def __init__(self,make,model,power):
        Car.__init__(self,make,model)
        self.power=power
class Rally(Car):
    def __init__(self,make,model,power):
        Car.__init__(self,make,model)
        self.power=power
class Classic(Car):
    def __init__(self,make,model,power):
        Car.__init__(self,make,model)
        self.power=power
class Hatch(Car):
    def __init__(self,make,model,power):
        Car.__init__(self,make,model)
        self.power=power