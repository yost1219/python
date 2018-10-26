class Person:

    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def Name(self):
        return self.firstname + " " + self.lastname

class Hero(Person):

    def __init__(self, first, last, heroName):
        Person.__init__(self,first, last)
        self.heroName = heroName

    def HeroName(self):
        return self.Name() + ", " +  self.heroName

x = Person("Mary Jane", "Watson")
y = Hero("Peter", "Parker", "Spider-Man")

print(x.Name())
print(y.HeroName())