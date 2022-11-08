# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def helper(self, node, p, q):
        if not node:
            return None
        # a node itself is its ancestor
        # a cut-off in postorder traversal
        if node == p or node == q:
            return node
        
        left = self.helper(node.left, p, q)
        right = self.helper(node.right, p, q)
        
        # if left and right contains p/q, it is ancestor
        if left and right:
            return node
        elif left or right:
            return left or right
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # preorder recursive, find the node whose subtrees contains p and q
        
        return self.helper(root, p, q)