# python inheritance

#Inheritance allows us to define a class that inherits all the methods and properties from
#another class.

#Parent class is the class being inherited from, also called base class.
#Child class is the class that inherits from another class, also called derived class.

class person:
    def __init__(self, fname,lname):
        self.firsname = fname
        self.lastname = lname
    
    def printname(self):
        print(self.firsname, self.lastname)
    
x = person('Mo','Asslahi')
x.printname()

#child class eg 

class student(person):
    def __init__(self, fname, lname):
        person.__init__(self,fname,lname)

student1 = student("Ahmed","Asslahi")
student1.printname()