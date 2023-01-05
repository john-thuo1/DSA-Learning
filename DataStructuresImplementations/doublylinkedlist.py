class Node:
    def __init__(self, data):
        self.data = data
        # next reference as nref
        self.nref = None
        # previous reference as pref
        self.pref = None


class Doublylinkedlist:
    def __init__(self):
        self.head = None
        
    def forwardTraversal(self):
        if self.head == None:
            return " Doubly Linked List is Empty"
        else:
            current = self.head
            while current != None:
                print(current.data, end=" ")
                current = current.nref
    def backwardTraversal(self):
        if self.head == None:
            return " Doubly Linked List is Empty"
        else:
            current = self.head
            while current.nref != None:
                current = current.nref
            
            while current != None:
                print(current.data, end=" ")
                # Move to the previous node and so forth.
                current = current.pref
    
    def addStart(self, data):
        newNode = Node(data)
        # If linked list is empty, new node becomes the new node
        if self.head is None:
            self.head = newNode
        else:
            newNode.nref = self.head
            self.head.pref = newNode
            self.head = newNode
        
    def addEnd(self, data):
        newNode = Node(data)
        # If Linked list is empty
        if self.head is None:
            self.head = newNode
        else:
            current = self.head
            # Loop till the end of the loop
            while current.nref !=None:
                current = current.nref
            
            # Change the last Node's Next reference to point to new node 
            current.nref = newNode 
            # Change the previous Ref of New Node to point to the initially last node   
            newNode.pref = current
        
node = Doublylinkedlist()
node.addStart(10)
node.addEnd(20)
print("Forward Traversal \ ")
node.forwardTraversal()   
print()  
print("Backward Traversal \ ")
node.backwardTraversal()       
        
        
            
                
            
                
            
            
            
        