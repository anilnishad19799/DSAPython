""" Lowest common ancestor """

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # if not root:
        #     return None

        # if p.val < root.val < q.val or q.val < root.val < p.val:
        #     return root

        # if p.val < root.val and q.val < root.val:
        #     self.lowestCommonAncestor(root.left, p, q)
        # if p.val > root.val and q.val > root.val:
        #     self.lowestCommonAncestor(root.right, p, q)


        if not root:
            return None

        if p.val <= root.val <= q.val or q.val <= root.val <= p.val:
            return root

        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
