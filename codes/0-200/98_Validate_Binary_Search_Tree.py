# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node):
        if not node:
            return True, float('-inf'), float('inf')
        
        left_flag, left_maximum, left_minimum = self.helper(node.left)
        right_flag, right_maximum, right_minimum = self.helper(node.right)
        if left_maximum >= node.val or right_minimum <= node.val or not left_flag or not right_flag:
            return False, float('inf'), float('-inf')
        else:
            return True, max(node.val, left_maximum, right_maximum), min(node.val, right_minimum, left_minimum)
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # postorder traversal. use two variables to store the maximum left and minimum right
        flag, maximum, minimum = self.helper(root)
        return flag