# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node: TreeNode) -> [bool, int]:
        if not node:
            return True, 0
        left_flag, left_depth = self.helper(node.left)
        right_flag, right_depth = self.helper(node.right)
        if not left_flag or not right_flag or abs(left_depth-right_depth)>1:
            return False, float('inf')
        else:
            return True, max(left_depth, right_depth)+1
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # postorder traversal recursive method, store the maximum depth of left and right tree
        flag, _ = self.helper(root)
        return flag