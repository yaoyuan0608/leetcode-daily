# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def helper(self, node):
        if not node:
            return False
        if self.helper(node.left):
            return True
        if self.tmp == self.p:
            self.res = node
            return True
        else:
            self.tmp = node 
        if self.helper(node.right):
            return True
        return False
    
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        # use two variable and do inorder traversal. tmp to store the previous node and res store the current one
        self.p = p
        self.tmp = None
        self.res = None
        self.helper(root)
        return self.res