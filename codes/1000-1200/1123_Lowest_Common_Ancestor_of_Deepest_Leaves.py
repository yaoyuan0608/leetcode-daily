# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node):
        if not node:
            return None, 0
        
        left, left_depth = self.helper(node.left)
        right, right_depth = self.helper(node.right)
        
        if left_depth == right_depth:
            return node, left_depth + 1
        elif left_depth > right_depth:
            return left, left_depth + 1
        else:
            return right, right_depth + 1
    
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # postorder traversal
        # if the left child is deeper, the LCA is in left tree
        return self.helper(root)[0]