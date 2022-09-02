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
        res = 1
        left = self.helper(node.left)
        right = self.helper(node.right)
        
        if node.left:
            if node.left.val - 1 == node.val:
                res = max(res, left + 1)
        if node.right:
            if node.right.val - 1 == node.val:
                res = max(res, right+1)
        self.output = max(self.output, res)
        return res
        
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        # recursive postorder
        self.output = 0
        self.helper(root)
        return self.output