# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_depth(self, node):
        if not node:
            return 0
        left = self.get_depth(node.left)
        right = self.get_depth(node.right)
        return 1 + max(left, right)
    
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # compare the depth of left tree and right tree
        # if the depth of left and righ tree are the same, the left tree must be full
        # else, the right tree must be full
        if not root:
            return 0
        left = self.get_depth(root.left)
        right = self.get_depth(root.right)
        if left == right:
            return pow(2, left) - 1 + 1 + self.countNodes(root.right)
        else:
            return pow(2, right) - 1 + 1 + self.countNodes(root.left)