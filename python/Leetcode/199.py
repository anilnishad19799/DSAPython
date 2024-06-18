""" Right size view problem """

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if root is None:
            return root

        queue = []
        result = []
        queue.append(root)

        while queue:
            qsize = len(queue)
            new = []
            while qsize>0:
                node = queue.pop(0)
                new.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
                qsize-=1
            
            if new:
                result.append(new[-1])
        
        return result