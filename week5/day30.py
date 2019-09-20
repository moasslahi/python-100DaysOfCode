# day 30 python Loops 3

# range function 
for x in range(6):
    print(x)

#starring from but not including
for x in range(2,6):
    print(x)

# increment
for x in range(2, 30, 3):
    print(x)

#else in for loop
for x in range(6):
    print(x)
else:
    print("finally finished")

#nested loop
adj = ["red","big","tasty"]
fruit = ["apple","banana","cherry"]

for x in adj:
    for y in fruit:
        print(x, y)
