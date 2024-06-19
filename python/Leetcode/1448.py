""" Good Node from tree """

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        """
        My Solution 

        def getcount(root):
            nonlocal maxvalue
            nonlocal count
            if root is None:
                return 0
            if root:
                maxvalue.append(root.val)
            getcount(root.left)
            getcount(root.right)

            if root.val >= max(maxvalue):
                count+=1
            maxvalue.pop()

        maxvalue = []
        count = 0
        getcount(root)

        return count
        """

        """ upgraded Solution """
        count = 0
        def getcount(root, maxvalue):
            nonlocal count
            if root is None:
                return 

            if root.val >= maxvalue:
                count+=1
                maxvalue = root.val

            getcount(root.left, maxvalue)
            getcount(root.right, maxvalue)

        getcount(root, float('-inf'))

        return count