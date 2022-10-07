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
        
        self.res = max(self.res, max(left, 0) + max(right, 0) + node.val)
        return max(max(left, 0), max(right, 0)) + node.val
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # recursive, every time check the sum of left value and right value
        self.res = float('-inf')
        self.helper(root)
        return self.res