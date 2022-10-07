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
        left_len = self.helper(node.left)
        right_len = self.helper(node.right)
        curr_left = 0
        curr_right = 0
        if node.left and node.left.val == node.val:
            curr_left = left_len + 1
        if node.right and node.right.val == node.val:
            curr_right = right_len + 1
        self.res = max(self.res, curr_left + curr_right)
        return max(curr_left, curr_right)
            
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        # recursive, use two variables to store the longest path of left and right tree
        self.res = 0
        self.helper(root)
        return self.res