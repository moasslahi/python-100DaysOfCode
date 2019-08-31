# Day 12 
text = "please, i want {} sandwishes and {} donuts"

#Adding 5 and 7 to the sentence using format()
sandwishes = 5
donuts = 7
text = text.format(sandwishes,donuts)

#Replacing "i" with "We" using replace()
text = text.replace("i","we")

#Replacing any "a" with "A" using replace()
text = text.replace("a","A")

#output
print(text)