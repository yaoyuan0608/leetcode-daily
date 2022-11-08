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
        if node in self.nodes:
            return node
        
        left_node = self.helper(node.left)
        right_node = self.helper(node.right)
        
        if left_node and right_node:
            return node
        elif left_node or right_node:
            return left_node or right_node
        
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        # similar to 236, postorder traversal
        # as we traverse from bottom to top, so we can make sure the last node is the ancestor
        
        self.nodes = nodes  
        return self.helper(root)