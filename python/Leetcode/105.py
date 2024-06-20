""" Implement a binary tree using inorder and preorder """

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        First approach to solve this problem

        if not inorder  or not preorder:
            return None
    
        root_val = preorder[0]
        root = TreeNode(root_val)

        inorderindex = inorder.index(root_val)

        leftinorder = inorder[:inorderindex]
        rightinorder = inorder[:inorderindex+1:]

        leftpreorder = preorder[1:1+len(leftinorder)]
        rightpreorder = preorder[1+len(leftinorder):]

        root.left = self.buildTree(leftpreorder, leftinorder)
        root.right = self.buildTree(leftpreorder, rightinorder)

        return root"""

        """
        Second approach better approach
        """

        inoderhash = {value:index for index, value in enumerate(inorder)}

        def makebt(leftpreorder, rightpreorder, leftinorder, rightinorder):
            if leftpreorder > rightpreorder:
                return None
            
            rootval = preorder[leftpreorder]
            root = TreeNode(rootval)
            rootindex = inoderhash[rootval]
            leftsubtreesize = rootindex - leftinorder

            root.left = makebt(leftpreorder+1, leftpreorder+leftsubtreesize, leftinorder, rootindex-1)
            root.right = makebt(leftpreorder+leftsubtreesize+1, rightpreorder, rootindex+1, rightinorder)

            return root

        return makebt(0, len(preorder)-1, 0, len(inorder)-1)
