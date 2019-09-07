# day 20 Python Sets 

#A set is a collection which is unordered and unindexed.
#In Python sets are written with curly brackets {}.

MySet =  {"Mo", "Football","Developer"}
print(MySet)

# looping through a set using for loop
for x in MySet:
    print(x)

MySet.add("Asslahi")   #add() accepts one item 
MySet.update(["Apple","Banana"]) # update() accepts multiple items 
print(MySet)