# day 28 Python loops

# while loop
i = 1
while i < 6:
    print(i)
    i += 1

#With the break statement we can stop the 
# loop even if the while condition is true.
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

#with the break statement we can stop the 
# loop even if the while condition is true.
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

