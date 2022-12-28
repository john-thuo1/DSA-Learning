
def collatzConjecture(n):
    iterations = 0
    listofNumbers = [n]
    while n!=1:
        
        if n %2 == 0:
            n = n/2
        elif (n%2 != 0): 
            n = (3*n) + 1
            
        iterations +=1
            
        listofNumbers.append(n)
    return f"{listofNumbers}. \nIt took {iterations} iterations to get to 1."

# print(collatzConjecture(7))

# Recursive implementation

def collatz(n, steps):
    collatzList = [n]
    steps+=1
    if n == 1 :
        return [1]                 
    elif n % 2 == 0 :
         
        collatzList.extend(collatz(n//2, steps))     
    else:
        collatzList.extend(collatz(n*3+1, steps))
         
    return collatzList

steps =0
print(collatz(7, steps))