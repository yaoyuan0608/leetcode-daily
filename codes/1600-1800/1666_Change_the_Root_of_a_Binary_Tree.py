"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def helper(self, child, node):
        if not node:
            return
        p = node.parent
        node.parent = child
        if not p:
            if node.left == child:
                node.left = None
            elif node.right == child:
                node.right = None
        else:
            if node.left == child:
                node.left = p
            elif node.right == child:
                node.right = node.left
                node.left = p
        self.helper(node, p)
        
    def flipBinaryTree(self, root: 'Node', leaf: 'Node') -> 'Node':
        # still confused, check discussion
        self.helper(None, leaf)
        return leaf