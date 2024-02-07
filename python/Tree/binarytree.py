class BinaryTreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data
    
    def getLeft(self):
        return self.left
    
    def getRight(self):
        return self.right
    

""" Recursive way"""
class BinaryTree:
    def __init__(self, root):
        self.root = root

    def preOrder(self, root):
        
        if root==None:
            return
        
        print("Data", root.data)
        self.preOrder(root.left)
        self.preOrder(root.right)

    def inOrder(self, root):
        if root == None:
            return
        
        self.InOrder(root.left)
        print("Data is ", root.data)
        self.inOrder(root.right)

    def postOrder(self, root):
        if root == None:
            return
        
        self.postOrder(root.left)
        self.postOrder(root.right)
        print("Data is ", root.data)

""" Iterative way"""
class BinaryTree:
    def __init__(self, root):
        self.root = root

    def preOrder(self):
        if not self.root:
            return
        
        stack = []
        result = []
        stack.append(self.root)

        while stack:
            node = stack.pop()
            result.append(node.data)
            
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)

