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
        node.left = None
        self.start.right = node
        self.start = node
        self.helper(node.right)
    def increasingBST(self, root: TreeNode) -> TreeNode:
        # inorder traversal
        self.head = self.start = TreeNode(None)
        self.helper(root)
        return self.head.right