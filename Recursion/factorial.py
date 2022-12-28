# Iterative Approacj
def factorial(num):
    factor = 1
    for i in range(1,num+1):
        if num <=1:
            return 1
        else:
            factor *=i
    return factor
        
  
def Factorial(num):      
    if num <=1:
        return 1
    return num * factorial(num-1)


print(factorial(5))
print(Factorial(5))
        