""" Is suntree """

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if root is None and subRoot is None:
            return True
        
        if root is None and subRoot is not None:
            return False
        
        if root is not None and subRoot is None:
            return False

        def isSametree(mainroot, subroot):
            if mainroot is None and subRoot is None:
                return True
            if mainroot is not None and subroot is None:
                return False
            if mainroot.val != subroot.val:
                return False
            
            isSametree(mainroot.left, subroot.left)
            isSametree(mainroot.right, subroot.right)
        
        return isSametree(root, subRoot)