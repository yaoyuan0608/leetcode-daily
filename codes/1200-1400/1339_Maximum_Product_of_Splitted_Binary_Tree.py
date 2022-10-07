# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def total(self, node):
        if not node:
            return
        self.total_sum += node.val
        self.total(node.left)
        self.total(node.right)
    def helper(self, node):
        if not node:
            return 0
        left = self.helper(node.left)
        right = self.helper(node.right)
        tmp = (left + right + node.val)
        self.res = max(self.res, tmp * (self.total_sum-tmp))
        return tmp
    
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        # count the total sum first, then calculate the sub sum of each sub tree
        self.total_sum = 0
        self.total(root)
        self.res = 0
        self.helper(root)
        return self.res%1000000007