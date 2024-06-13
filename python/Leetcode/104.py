""" get height of tree """

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        else:
            lcount = self.maxDepth(root.left)
            rcount = self.maxDepth(root.right)
        
        if lcount > rcount:
            return 1 + lcount
        else:
            return 1 + rcount