""" Is suntree """

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if subRoot is None:
            return 1
        if root is None:
            return 0
        
        if self.isSametree(root, subRoot):
            return 1
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSametree(self, mainroot, subroot):
        if mainroot is None and subroot is None:
            return 1
        if mainroot is None or subroot is None:
            return 0
        if mainroot.val != subroot.val:
            return 0
        
        return self.isSametree(mainroot.left, subroot.left) or self.isSametree(mainroot.right, subroot.right)