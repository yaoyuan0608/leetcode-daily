# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, should_max):
        if not node:
            return 
        self.max = max(self.max, should_max)
        self.count += 1
        self.dfs(node.left, should_max*2)
        self.dfs(node.right, should_max*2+1)
        
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
    # dfs: preorder, add 1 to global count at each node, determine global count == maximum should reach
    # for its left node, maximum count is 2*count, right maximum is 2*count+1
        self.max = 0
        self.count = 0
        self.dfs(root, 1)
        return self.count == self.max