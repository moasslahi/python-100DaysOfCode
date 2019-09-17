# day 29 Python loops 2 

fruits = ["Apple","Banana","Cherry"]
for x in fruits:
    print(x)

#looping through a string
for x in "banana":
    print(x)

#break statement
for x in fruits:
    print(x)
    if x == "Banana":
        break

#continue statement
for x in fruits:
    if x == "Banana":
        continue
    print(x)
