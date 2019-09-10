# Day 23 python Dictionaries 2
MyDict = {
    "Name": "Mo Asslahi",
    "FavFood": "Kabsa",
    "Hobby": "Football"
}

# to check a specific key is present
if "Name" in MyDict:
    print("Yes, 'Name' is one of the keys")
else:
    print("No, 'Name' is not of the keys'")

# dictionary length
print(len(MyDict))

#Adding items
MyDict["LovePython?"] = True
print(MyDict)

#Removing items
MyDict.pop("FavFood")
print(MyDict)

# Deleting the whole dictioary
del MyDict

#emptying the dictionary 
MyDict.clear()
print(MyDict)


