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
        self.helper(node.right)
        self.res.append(node.val)
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # left, right, curr
        self.res = []
        self.helper(root)
        return self.res