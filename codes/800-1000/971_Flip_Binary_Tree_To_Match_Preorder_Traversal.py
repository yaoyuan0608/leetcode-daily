# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node):
        if not node or self.idx == len(self.voyage):
            return
        if node.val != self.voyage[self.idx]:
            self.res = [-1]
            return 
        self.idx += 1

        if node.left and node.left.val != self.voyage[self.idx]:
            self.res.append(node.val)
            self.helper(node.right)
            self.helper(node.left)
        else:
            self.helper(node.left)
            self.helper(node.right)
            
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        # do pre-order traversal. if current node is different from the next voyage value, return -1
        # if current node has left child but its value is different from the next voyage, flip left and right
        self.res = []
        self.voyage = voyage
        self.idx = 0
        self.helper(root)
        if self.res and self.res[0] == -1:
            return [-1]
        else:
            return self.res