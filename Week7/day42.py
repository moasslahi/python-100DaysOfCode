# Day 42 Python Classes and objects

#objects method 

class person:
    def __init__(self, name,age):
        self.name = name
        self.age = age
    
    def Myfunc(self):
        print("Hello my name is " + self.name)

person1 = person('Mo', 36)
person1.Myfunc()

#modify objetcs properties
person1.name = 'Ahmed'
print(person1.name)

#delete object properties 
del person1.age

#delete objects
del person1