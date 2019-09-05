#day 17 python tuple 2 
thistuple = ("apple","banana","Cherry")

# to check if something is in the tuple 
if "Apple" in thistuple:
    print("yes, 'Apple' is in the fruits tuple")

# to repeat item
thistuple2 = ("Mo",) * 3 
print(thistuple2)

# to add 2 or more tuples into one tuple
tuple1 = (1,2,3)
tuple2 = (4,5,6)
tuple1and2 = tuple1 + tuple2 
print(tuple1and2)

#to determine how many items a tuple has 
thistuple = ("apple","banana","Cherry")
print(len(thistuple))