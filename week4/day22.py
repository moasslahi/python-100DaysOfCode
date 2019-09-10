#Day 22 python Dictionaries 

'''
A dictionary is a collection which is unordered,
changeable and indexed.
In Python dictionaries are written with curly brackets {}
, and they have keys and values.
'''

MyDict = {
    "Name": "Mo Asslahi",
    "Hobby": "Football",
    "FavFood": "Kabsa"
}
print(MyDict)

#accessing items
Myname = MyDict["Name"] #2, Mydict.get("Name")
print(Myname)

#changing values
MyDict["FavFood"] = "Pasta"

#looping through a dictionary 
for x in MyDict:
    print(MyDict[x])

for x, y in MyDict.items():
    print(x,y)

