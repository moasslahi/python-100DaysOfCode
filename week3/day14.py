# Day 14 python lists 2

#print part of the list
thislist = ["a","b","c","d"]
print(thislist[1:3])

#to check if something is in the list
if "a" in thislist: 
    print("yes,'a' is in the list")

#to repeat item in a list
newlist = ["mo"] *4
print(newlist)

#to add 2 or more lists together
AllLists = thislist + newlist
print(AllLists)