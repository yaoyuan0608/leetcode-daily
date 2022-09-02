# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node):
        if not node:
            return
        left = self.helper(node.left)
        right = self.helper(node.right)
        node.left = right
        node.right = left
        return node
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.helper(root)