def fibonacci(idx):
    if idx == 1:
        return 1
    elif idx ==2:
        return 1
    else:
        return fibonacci(idx-1) + fibonacci(idx-2)

# for i in range(1, 10+1):
#     print(fibonacci(i), end=" ")
    
#Memoization - stores values of previous function calls such that the function won't repeat itself 
# in computing previous calls and instead retrieves the values stored.add()

fibonacci_cache = {}

def Fibonacci(n):
    # If number already in the dictionary, return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    
    if n  == 1:
        return 1
    if n == 2:
        return 1
    elif n > 2:
        value = Fibonacci(n-1) + Fibonacci(n-2)
    
    # Add the number to the cache
    fibonacci_cache[n] = value
    
    return value

# for i in range(1,101):
#     print(Fibonacci(i), end=" ")

from functools import lru_cache
@lru_cache(maxsize = 1000)
def fibonacci(idx):
    if type(idx) != int:
        raise TypeError("idx must be an integer")
    if idx <1:
        raise ValueError("idx must be a positive integer")
    if idx == 1:
        return 1
    elif idx ==2:
        return 1
    else:
        return fibonacci(idx-1) + fibonacci(idx-2)

for i in range(1, 1000):
    print(fibonacci(i), end=" ")





        



        