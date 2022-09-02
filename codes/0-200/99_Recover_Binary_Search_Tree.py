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
        self.helper(node.left)
        if not self.val1 and self.pivot.val > node.val:
            self.val1 = self.pivot
        if self.val1 and self.pivot.val > node.val:
            self.val2 = node
        self.pivot = node
        self.helper(node.right)
        
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # inorder traversal, compare current node the previous node
        self.pivot = TreeNode(float('-inf'))
        self.val1 = None
        self.val2 = None
        self.helper(root)
        
        self.val1.val, self.val2.val = self.val2.val, self.val1.val