# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node1, node2, level):
        if not node1 or not node2:
            return 
        if level % 2 == 0:
            
            val = node1.val
            node1.val = node2.val
            node2.val = val            
            
        self.helper(node1.left, node2.right, level+1)
        self.helper(node1.right, node2.left, level+1)
         
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or not root.left:
            return root
        self.helper(root.left, root.right, 0)
        return root