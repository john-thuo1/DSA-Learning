#Stack implementation using a List
# The method assumes that the end of the list as the top

class Stack:
    def __init__(self):
        # Initialize an empty stack
        self.items = []
    
    def isEmpty(self):
        return self.items ==[]
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    # check the index of the last item in the list i.e top element of the list
    # To do this, we get length of stack and minus 1. 
    # return value at self.items[len(self.items)-1]
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)
    
# obj = Stack()
# obj.push(2)
# obj.push(5)
# obj.push(7)
# obj.push('John')


# print(obj.peek())
# print(obj.isEmpty())