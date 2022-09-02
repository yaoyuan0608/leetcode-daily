# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node):
        if not node:
            return None
        self.helper(node.right)
        self.helper(node.left)
        node.right = self.prev
        node.left = None
        self.prev = node
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # postorder traversal, reverse of preorder
        if not root:
            return []
        self.prev = None
        self.helper(root)
        return self.prev.right