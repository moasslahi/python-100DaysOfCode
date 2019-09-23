# Day 34 Python Functions 2 

# parameters
def my_function(food):
    for x in food:
        print(x)

fruits = ["apple","cherry"]

my_function(fruits)

#return a value
def my_functionx (x):
    return 5 * x 
print(my_functionx(10))

#keyword argument
def my_functiony(Child3,Child2,Child1):
    print("The youngest child is " + Child3)

my_functiony(Child1 = "Emil", Child2 = "Mo", Child3 = "Ahmed")

#Recursion
def tri_recursion(k):
    if(k>0):
        result = k+tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result
print("\n\nRecursion Example Results")
tri_recursion(6)