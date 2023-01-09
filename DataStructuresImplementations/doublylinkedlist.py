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

    def addAfter(self, xNode, data):
        # Check if list is empty or not
        if self.head is None:
            return "Doubly Linked list is empty"
        else:
            current = self.head
            # You will be able to exit the loop on 2 conditions :
            # 1. If the current node is None or if current.data is equal to xNode value
            while current !=None:
                if current.data == xNode:
                    break
                current = current.nref
            
            if current is None:
                return "Given Node is not Proesent in the Doubly Linked List"
            else:
                # Create the New Node
                newNode = Node(data)
                # New Node should store the reference of the next node
                # which is currently stored at current.nref
                newNode.nref = current.nref
                # New Node previous reference should point to the current node
                newNode.pref = current
               
               # Checks if we are inserting the new node after the last node 
                if current.nref is not None:
                    #The node that is after the New Node should 
                    # store the reference to the new node in its pref
                    current.nref.pref = newNode
                    
                    # Current Node next reference should store the new node reference
                current.nref = newNode
                
                
            
    def addBefore(self, xNode, data):
        # Check if list is empty or not
        if self.head is None:
            return "Doubly Linked list is empty"
        else:
            current = self.head
            # You will be able to exit the loop on 2 conditions :
            # 1. If the current node is None or if current.data is equal to xNode value
            while current !=None:
                if current.data == xNode:
                    break
                current = current.nref
            
            if current is None:
                return "Given Node is not Proesent in the Doubly Linked List"            
            else:
                newNode = Node(data)
                newNode.nref = current
                
                newNode.pref = current.pref
                if current.pref is not None:
                    current.pref.nref = newNode
                else:
                    self.head = newNode
                    
                current.pref = newNode
                
                       
node = Doublylinkedlist()
node.addStart(10)
node.addEnd(20)
print("Forward Traversal \ ")
node.forwardTraversal()   
print()  
print("Backward Traversal \ ")
node.backwardTraversal()       
        
        
            
                
            
                
            
            
            
        