""" Balanced binary search tree """

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getheightoftree(root):
            nonlocal balancetree
            if root is None:
                return 0
            else:
                lcount = getheightoftree(root.left)
                rcount = getheightoftree(root.right)

            if abs(lcount - rcount) > 1:
                balancetree = False
            
            return max(lcount, rcount) + 1

        balancetree = True
        getheightoftree(root)
        return balancetree