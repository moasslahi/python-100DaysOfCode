thislist = ["apple","banana","cherry"]

#the len() method determines how many items a list has
print(len(thislist))

#the append() method adds an item to the end of the list
thislist.append("orange")
print(thislist)

#the insert() method adds an item at the specified index
thislist.insert(1,"strawberry")
print(thislist) 

#The remove() method removes the specified item.
thislist.remove("banana")
print(thislist)

#The pop() method removes the specified index.
thislist.pop()
print(thislist)

#The clear() method empties the list.
thislist.clear()
print(thislist)

#ways to copy a list
Mylist = thislist.copy() #1
Mylist = list(thislist) #2

