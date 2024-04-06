
""" Insertion and Deletion of Binary Search Tree"""

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def setData(self, data):
        self.data =  data
        return self.data
    
    def getData(self):
        return self.data
    

class BinarySearchTree:
    def _init_(self):
        self.root =  None

    def insertion(self, root, data):
        if root is None:
            # print("INintially None")
            return BSTNode(data)
        else:
            if data < root.data:
                # print("In Left")
                if root.left is None:
                    # print("In Left both None")
                    root.left = BSTNode(data)
                else:
                    # print("insertion Left")
                    root.left = self.insertion(root.left, data)

            elif data > root.data:
                # print("In Right")
                if root.right is None:
                    # print("In Right both None")
                    root.right = BSTNode(data)
                    # return root
                else:
                    # print("insertion Right")
                    root.right = self.insertion(root.right, data)
        return root
    
    def findMin(self, root):
        if root.left is None:
            # print("IN",root.data)
            return root
        else:
            print(root.data)
            root = self.findMin(root.left)
        
        return root
    
    def deletion(self, root, data):
        if root is None:
            return None
        
        if data < root.data:
            root.left = self.deletion(root.left, data)
        elif data > root.data:
            root.right = self.deletion(root.right, data)
        else:
            if root.left is None and root.right is None:
                # root.data = None
                return None
            elif root.left is None:
                # pass
                root = root.right
                return root
            elif root.right is None:
                root = root.left
                return root
            else:
                findminsuccessor = self.findMin(root.right)
                # print("findminsuccessor", findminsuccessor.data)
                root.data = findminsuccessor.data
                root.right = self.deletion(root.right ,findminsuccessor.data)

        return root


bstobj = BinarySearchTree()
root = None
root = bstobj.insertion(root, 10)
root = bstobj.insertion(root, 20) 
root = bstobj.insertion(root, 8)
root = bstobj.insertion(root, 6)
root = bstobj.insertion(root, 19)
root = bstobj.insertion(root, 34)
root = bstobj.insertion(root, 11)   
root = bstobj.insertion(root, 40)   
root = bstobj.insertion(root, 12)   
print(root.data)


""" how can we say that the tree is generated is correct or not"""
""" We implement Inorder Tree and if it is giving all value in sorted order then it is binary search tree"""

def inOrder(root):
    if root is None:
        return None
    inOrder(root.left)
    print(root.data)
    inOrder(root.right)
inOrder(root)