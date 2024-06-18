""" Problem of level order traversal """

from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return root
        queue = []
        level = 0
        resultlist = []
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
                
            resultlist.append(new)

            level+=1

        return resultlist