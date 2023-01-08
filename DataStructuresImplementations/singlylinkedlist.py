# Singly Linked List Implementation

class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class linkedList:
    def __init__(self):
        # It is empty. No nodes in the Linked List.
        self.head = None
        
    # def addstart(self, data):
    def traverse(self):
        if self.head == None:
            return "Singly Linked List is empty"
        else:
            n = self.head
            # n. data is data in the node
            # n.ref is address to the next node
            # n=n.ref moves us to the reference of the next node
            # We will use a while loop given that we know the stopping condition
            # Our Stopping condition will be n !=None
            while n != None:
                print(n.data, end=" ")
                # Move to the next node
                n = n.ref
                
    def addStart(self, data):
        newNode = Node(data)
        newNode.ref = self.head
        self.head =newNode
    
    def addEnd(self, data):
        # Create a node
        newNode = Node(data)
        if self.head == None:
            self.head = newNode 
        else:
            n = self.head    
            while n.ref is not None:
            # Go upto the last node where reference is Null
                n = n.ref
                
            # Change the reference of the last node to the newly created node/
            n.ref = newNode
    # x represents the previous node of the linked list
    def addMiddle(self, data, x):           
        n = self.head
        while n is not None:
            # If you have found the x value, exit the loop
            if x == n.data:
                break
            # If you have not found the x value, move to the next node
            n = n.ref
        # You exit the loop on 2 conditions: if x is None/ does not exist in the loop 
        # And when you find x value equal to the number you had passed as an argument
        if n is None:
            return "Node is not present in the Singly Linked List"
        
        # And when you find x value equal to the number you had passed as an argument
    
        else:
            newNode = Node(data)
            # New Node should refer to the next node reference stored in n node(n.ref)
            newNode.ref = n.ref
            # Node x's reference should then point to newNode
            n.ref = newNode
            
        # The code below only works when you have x value in the Linked List
        # newNode = Node(data)
        # while n.data != x:
        #     n = n.ref
        # newNode.ref = n.ref
        # n.ref = newNode
    def deleteStart(self):
        if self.head == None:
            return " Singly Linked List is Empty!"
        else:
            # second node whose reference is stored in the head node,
            # becomes the new head node.
            self.head = self.head.ref
    def deleteEnd(self):
        if self.head == None:
            return "Singly Linked List is Empty"
        elif self.head.ref is None:
            self.head = None
        else:
            current = self.head 
            # current.ref contains the reference of the next node 
            # A -> B  current node is A. reference of B - current.ref
            # current.ref.ref contains the reference of the node after 
            # A -> B -> C  returns the reference of C
            
            while current.ref.ref != None:
                current = current.ref
            current.ref = None
            
    def size(self):
        count =0
        current = self.head
        while current != None:
            count +=1
            current = current.ref
            
        return count
    
    def reverse(self):
        # Uses 3 pointers to reverse the linked list
        previous = None
        current = self.head
        while current != None:
            next = current.ref
            current.ref = previous
            previous = current
            current = next
        self.head = previous 
        print("\n\nReversed Link is : ")
        self.traverse()
    
    def findNode(self, data):
        current =self.head
        while current !=None:
            if current.data == data:
                return "Node exists in the Linked List!"
            current = current.ref
        
        return "Element does not exist in the Linked List!"
                      
        
node = linkedList()
node.addStart(10)
node.addStart(11)
node.addStart(12)
node.addStart(13)
node.addStart(14)
node.addEnd(15)
node.addMiddle(5, 12)
node.deleteEnd()
node.traverse()

node.reverse()
print()

print("Number of nodes in the Linked list is : ", node.size())
print()
print(node.findNode(115))
    
        
        
            
            
            
        
        
        