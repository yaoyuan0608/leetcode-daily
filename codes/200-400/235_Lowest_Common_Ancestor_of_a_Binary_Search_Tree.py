# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def helper(self, node):
        if not node:
            return None
        if node.val == self.p.val or node.val == self.q.val:
            return node
        if node.val > self.p.val and node.val < self.q.val:
            return node
        elif node.val < self.p.val:
            return self.helper(node.right)
        else:
            return self.helper(node.left)
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # if root value is between p and q, it is their ancestor
        # preorde traversal
        if p.val > q.val:
            self.p = q
            self.q = p
        else:
            self.p = p
            self.q = q
        
        return self.helper(root)