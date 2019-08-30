#Day 11 python operators 2 

#logical operators are used to combine conditional statements.
x = 3
x < 5 and x < 10 # and
x < 5 or x < 4 # or
not(x < 5 and x < 10) # not

#Python Identity Operators compare the objects, if
#they are actually the same object, with the same memory location.

a = ["apple","banana"]
b = ["apple","banana"]
z = a

print(z is a)
print(z is not a)

#Membership operators are used to test 
# if a sequence is presented in an object.
d = ["apple","banana"]

print("apple" in d)
print("apple" not in d)
