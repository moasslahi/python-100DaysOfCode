# Day 9 string format 

'''
We can combine strings and numbers by using the format() method!
The format() method takes the passed arguments, formats them, 
and places them in the string where the placeholders { } are.
'''

age = 18 
txt = "My name is Mo, and i am {}"
print(txt.format(age))

quantity = 3
itemNum = 123
price = 25
MyOrder = " i want {} pieces of item {} for {} dollars"
print(MyOrder.format(quantity,itemNum,price))