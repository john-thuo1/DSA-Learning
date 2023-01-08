# To create a node, use this class
class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None
    
class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def traversal(self):
        if self.head == None:
            return "Linked List is Empty"
        else:
            current = self.head
            while current != None:
                print(current.data)
                current = current.ref
    def addStart(self, data):
        newNode = Node(data)
        if self.head is None:
            newNode = self.head
        else:
            # 2nd Case, where linked list is not empty
            # Change the reference of the new node to point to self.head
            newNode.ref = self.head
            self.head = newNode
    def addMiddle(self,xNode,data):
        # xNode represents the data of the node we want to add our newnode  e.g xNode = 5. 
        # We want to add data after 5
        newNode = Node(data)
        current = self.head
        while current !=None:
            if xNode == current.data:
                break
            current = current.ref
            
        # You exit the loop on 2 conditions: if x is None/ does not exist in the loop 
        # And when you find x value equal to the number you had passed as an argument
        if current is None:
            return "Node is not in the linked list"
        
        # And when you find x value equal to the number you had passed as an argument
        else:
            # The new Node's reference should refer to the next node hence current.ref
            newNode.ref = current.ref
            
            # Current Node's reference  should refer to the new node.
            current.ref = newNode 
            
    def addEnd(self, data):
        newNode = Node(data)
        if self.head is None:
            newNode = self.head
        else:
            current = self.head
            while current.ref != None:
                current = current.ref
            current.ref = newNode
        
    def sizeofLL(self):
        count = 0
        current = self.head
        while current!= None:
            count +=1
            current = current.ref
        return count
    
    def reverseSinglyLinkedList(self):
        previous =0
        current = self.head
        while current !=None:
            next = current.ref
            current.ref = previous
            previous = current
            current = next
        self.head = previous
        print("\n\nReversed Link is : ")
        self.traversal()
    def find(self, data):
        current = self.head
        while current != None:
            if current.data == data:
                return "Node Exists in the Linked List"
            current = current.ref
        return "No Such Node in the Linked List"
    
    def deleteStart(self):
        current = self.head
        if current == None:
            return " Singly Linked List is Empty"
        else:

            # second node whose reference is stored in the head node,
            # becomes the new head node.
            current = current.ref 
            
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
    
    def deleteAny(self, data):
        # First Check if the LL is empty
        if self.head == None:
            return "Singly Linked List is Empty!"
        # If the data of the node we want to delete is the first node, 
        # then use deleteStart method
        if self.head.data == data:
            self.deleteStart()
        else:
            current = self.head
            while current.ref != None:
                if current.ref.data == data:
                    break
                current = current.ref
            if current.ref is None:
                return " No such node exists in the Singly Linked List"
            else:
                # Change the reference of the previous node to refer to the node which comes after the one you are deleting
                current.ref = current.ref.ref
            
        
        
    
    

            
            
            
        
            
        
                
                
    
