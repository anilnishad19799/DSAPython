""" Get diameter of tree """

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def __init__(self):
        diameter = 0

        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def getheightoftree(node: Optional[TreeNode]) -> int:
            nonlocal diameter
            if not node:
                return 0
            
            # Recursively find the height of the left and right subtrees
            lheight = getheightoftree(node.left)
            rheight = getheightoftree(node.right)
            
            # Update the diameter if the path through the current node is longer
            diameter = max(diameter, lheight + rheight)
            
            # Return the height of the tree rooted at the current node
            return max(lheight, rheight) + 1
        
        # Call the helper function to initiate the recursive traversal
        diameter = 0
        getheightoftree(root)
        return diameter