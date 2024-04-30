from binarysearchtreeinsertiondeletion import BinarySearchTree

class BSTHeightTree:
    def __init__(self):
        self.root = None
    
    def getHeightOfTree(self, root):
        if root is None:
            return 0
        
        else:
            leftcount = self.getHeightOfTree(root.left)
            rightcount = self.getHeightOfTree(root.right)

        if leftcount>rightcount:
            return 1 + leftcount
        else:
            return 1 + rightcount
        
""" import binary tree insertion and deletion """
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
# root = bstobj.insertion(root, 12)   

heightobj = BSTHeightTree()
maxheight = heightobj.getHeightOfTree(root)
print("max height", maxheight)
