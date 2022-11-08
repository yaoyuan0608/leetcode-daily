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

        left = self.helper(node.left, p, q)
        right = self.helper(node.right, p, q)
        
        if node == p or node == q:
            self.count += 1
            return node
        
        elif left and right:
            return node
        elif left or right:
            return left or right
        else:
            return None
            
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # similar to 236, do postorder traversal to go through all the nodes
        # need to use a tracker to track the existance of p and q
        self.count = 0

        node = self.helper(root, p, q)
        if self.count == 2:
            return node
        else:
            return None