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
        if node.val == self.prev:
            self.cur_max += 1
        else:
            self.cur_max = 1
        if self.cur_max == self.maximum:
            self.res.append(node.val)
        elif self.cur_max > self.maximum:
            self.res = [node.val]
            self.maximum = self.cur_max
        self.prev = node.val
        self.helper(node.right)
        
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        # inorder travesal, every time keep track of the value of previous node, if same, add one
        self.res = []
        self.maximum = 0
        self.cur_max = 0
        self.prev = None
        self.helper(root)
        return self.res