#  Day 41 Python Classes and Objects 

#creating class
class Myclass:
    x = 5
print(Myclass)

#creating object
class Myclass:
    x = 5
p1 = Myclass()
print(p1.x)


# the __init__() function 
class person:
    def __init__(self,name,age):  
        self.name = name
        self.age = age

person1 = person("Mo", 18)

print(person1.name)
print(person1.age)


