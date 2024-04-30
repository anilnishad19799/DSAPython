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
    
class BinaryTree:
    def __init__(self, root):
        self.root = root

    def insert(self, data):
        newnode  = BinaryTreeNode(data)
        if self.root == None:
            self.root = newnode
            return
        
        node = self.root
        if data < node.data:
            if node.left is None:
                node.left = newnode
            else:
                self.insert(node.left)
        else:
            if node.right is None:
                node.right = newnode
            else:
                self.insert(node.right)
