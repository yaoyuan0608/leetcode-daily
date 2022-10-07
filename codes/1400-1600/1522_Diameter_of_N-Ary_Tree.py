"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def helper(self,node):
        if not node:
            return 0
        max1, max2 = 0, 0

        for child in node.children:
            child_depth = self.helper(child) + 1
            if child_depth > max1:
                max1, max2 = child_depth, max1
            elif child_depth > max2:
                max2 = child_depth
                
        self.max = max(self.max, max1+max2)
        return max1
    
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        # recursive, need two varibale to find the longest subtree within the children
        self.max = 0
        self.helper(root)
        return self.max