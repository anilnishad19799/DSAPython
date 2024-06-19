""" Kth smallest element from binary search tree """

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        if not root:
            return root
        
        allvalue = []

        queue = []
        queue.append(root)
        while queue:
            node = queue.pop()
            allvalue.append(node.val)

            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)
        
        return sorted(allvalue)[k-1]
        