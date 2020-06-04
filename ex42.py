class Animal(object):
    pass

class Dog(Animal):

    def __init__(self, name):
        self.name = name

class Person(object):

    def __init__(self, name):
        self.name = name
        self.pet = None

p = Person('joe')
p.pet = Dog('hack')

dog = Dog
print(dog is Dog)

