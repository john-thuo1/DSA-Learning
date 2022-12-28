class binaryTree:
    
    def __init__(self, root):
        self.root = root
        self.leftChild = None
        self.rightChild = None
        
    def insertLeft(self, newNode):
        if self.leftChild ==None:
            self.leftChild = binaryTree(newNode)
            
        else:
            value = binaryTree(newNode)
            value.leftChild = self.leftChild
            self.leftChild=value
            
    def insertRight(self, newNode):
        if self.rightChild ==None:
            self.rightChild = binaryTree(newNode)
        
        else:
            value = binaryTree(newNode)
            value.rightChild= self.rightChild
            self.rightChild = value
    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,root):
        self.root = root

    def getRootVal(self):
        return self.root
 
r = binaryTree('a')
print(r.getRootVal())
r.insertLeft('b')
print(r.getLeftChild().getRootVal())
r.insertRight('c')
r.insertLeft('d')
r.insertRight('e')
# print(r.getRightChild())
# print(r.getRightChild().getRootVal())
# r.getRightChild().setRootVal('hello')
# print(r.getRightChild().getRootVal())          
    
            
    
        
        
    