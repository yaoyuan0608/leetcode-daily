# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node):
        # validation, size, minimum, maximum
        if not node:
            return True, 0, float('inf'), float('-inf')
        else:
            l_validation, l_size, l_minimum, l_maximum = self.helper(node.left)
            r_validation, r_size, r_minimum, r_maximum = self.helper(node.right)
            if l_validation and r_validation and l_maximum < node.val < r_minimum:
                # if current node is a valid bst, backtrack the minimum and maximum of this tree
                self.res = max(self.res, l_size + r_size + 1)
                return True, l_size + r_size + 1, min(node.val, l_minimum), max(node.val, r_maximum)
            else:
                return False, 0, min(node.val, l_minimum, r_minimum), max(node.val, l_maximum, r_maximum)
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        # every time we trasverse a node, we need several variables:
        # first flag store the current node is a valid bst
        # second flag is to store the total size of tree
        # two local varibales to store the max and min of current tree
        self.res = 0
        flag, count, minimum, maximum = self.helper(root)
        return self.res