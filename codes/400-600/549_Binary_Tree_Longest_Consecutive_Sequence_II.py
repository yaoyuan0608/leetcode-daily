# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node):
        # increasing, decreasing
        if not node:
            return 0, 0
        inc, dec = 1, 1
        left_inc, left_dec = self.helper(node.left)
        right_inc, right_dec = self.helper(node.right)
        if node.left:
            if node.left.val + 1 == node.val:
                inc = max(inc, left_inc+1)
            if node.left.val - 1 == node.val:
                dec = max(dec, left_dec+1)
        if node.right:
            if node.right.val + 1 == node.val:
                inc = max(inc, right_inc+1)
            if node.right.val - 1 == node.val:
                dec = max(dec, right_dec+1)
        # current maximum length: left -> node -> right
        self.res = max(self.res, inc+dec-1)
        return inc, dec
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        # use two variables to store the longest increasing/decresing sequence at each node
        # the result of one node is decided by its left and right node, so postorder traversal
        self.res = 0
        self.helper(root)
        return self.res