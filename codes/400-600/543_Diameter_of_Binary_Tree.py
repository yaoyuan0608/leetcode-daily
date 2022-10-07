# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node):
        if not node:
            return 0
        left = self.helper(node.left)
        right = self.helper(node.right)
        
        self.res = max(self.res, left + right)
        return max(left, right) + 1
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # recursive. store the longest distance of left and right tree
        self.res = 0
        self.helper(root)
        return self.res