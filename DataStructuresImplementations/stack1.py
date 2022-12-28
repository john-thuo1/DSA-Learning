from stack import Stack
    
def reverse(mystr):
    myStack = Stack()
    reversedString = ""
    for char in mystr:
        myStack.push(char)
    
    while not myStack.isEmpty():
        reversedString += myStack.pop()
        
    return reversedString
        
    
        
    

    
    
    

print(reverse('John'))