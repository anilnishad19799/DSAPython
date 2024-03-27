""" Implementing binary search tree"""

class binarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def setdata(self, data):
        self.data = data

    def getdata(self):
        return self.data
    
    def getLeft(self):
        return self.left
    
    def getRight(self):
        return self.right
    


""" finding an element from binary search tree iterative"""

class findElement:
    def find(self, data):
        currentnode = self.root

        while currentnode != None or currentnode.data != data:
            if currentnode.data < data:
                currentnode = currentnode.left
            else:
                currentnode = currentnode.right
            
        return currentnode

""" finding an element from binary search tree in recursive way """

class findELementRecursive:
    def find(self, data):
        currentnode = self.root

        while currentnode:
            if currentnode.data == data:
                return currentnode.data
            
            if currentnode.data < data:
                currentnode = currentnode.left
            else:
                currentnode  =  currentnode.right

        return None
    

""" find minimum value from BST"""
# class MinMaxValueFromBST:
def minValue(self, root):
    ## base case define here
    currentNode = root
    if currentNode.left is None:
        return currentNode
    else:
        return minValue(currentNode.left)
                
            
def maxValue(self, root):
    currentNode = root

    if currentNode.right is None:
        return currentNode
    else:
        maxValue(currentNode.right)


def insert(root, node):
    if root == None:
        root = node
    else:
        if root.data > node.data:
            if root.left==None:
                root.left = node
            else:
                insert(root.left, node)
        else:
            if root.data < node.data:
                if root.right == None:
                    root.right = node
            else:
                insert(root.right, node)
                











