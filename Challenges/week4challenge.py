# week4 python challenge

#1
Myset = {1,3,5,7,8}

Myset.update([4,8,12])
Myset.remove(8)
Myset.clear()
print(Myset)


#2
Mydict = {
    "name": "pigeon",
    "type": "bird",
    "skin cover": "feathers"
}


print(Mydict.get("type"))
Mydict["skin cover"] = "new skin"
print(Mydict)