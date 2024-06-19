""" check if is a valid binary search tree"""

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        """ First Solution

        value = []
        def inorder(root):
            nonlocal value
            if root is None:
                return
            inorder(root.left)
            value.append(root.val)
            inorder(root.right)
        
        inorder(root)

        for i in range(len(value)-1):
            if value[i+1] < value[i]:
                return False
        
        return True
        """

        """
        This approach doesnot work here below one

        if root is None:
            return True

        if root.left:
            if root.left.val > root.val:
                return False
        if root.right:
            if root.right.val < root.val:
                return False

        return self.isValidBST(root.left) and self.isValidBST(root.right)

        """