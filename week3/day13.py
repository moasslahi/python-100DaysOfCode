#day 13 Python Lists 

#A list is a collection which is ordered and changeable []

numbers = [1,2,3,4,5]
print(numbers)

thislist = ["Apple", "banana", "cherry"]
print(thislist)

#To access an item
print(thislist[1])

#looping through a list 
for x in thislist:
    print(x)

#To change an item
thislist[1] = "Strawberry"
print(thislist)

#to delete an item of the list or the whole list 
del thislist[0]
print(thislist)





