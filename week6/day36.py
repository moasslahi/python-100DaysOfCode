# python lambda 2

#The power of lambda is better shown when you use them 
# as an anonymous function inside another function.

def myfunc(n):
    return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))