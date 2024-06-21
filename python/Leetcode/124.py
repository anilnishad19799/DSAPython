""" Find binary tree maximum path sum """


from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxvalue = float('-inf')
        
        def findmaxvalue(node):
            nonlocal maxvalue
            if node is None:
                return 0 
                
            leftmax = findmaxvalue(node.left)
            rightmax = findmaxvalue(node.right)

            leftmax = max(leftmax, 0)
            rightmax = max(rightmax, 0)

            maxvalue = max(maxvalue, node.val + leftmax + rightmax)

            return node.val + max(leftmax, rightmax)
        
        findmaxvalue(root)
        return maxvalue