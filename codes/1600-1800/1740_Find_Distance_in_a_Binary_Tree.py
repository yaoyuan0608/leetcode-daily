# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node, p, q):
        if not node:
            return -1
        
        left = self.helper(node.left, p, q)
        right = self.helper(node.right, p, q)

        if node.val == p or node.val == q:
            if left < 0 and right < 0:
                return 0
            else:
                self.res = 1 + max(left, right)
                return -1
        # p/q in subtrees, find the result
        if left >= 0 and right >= 0:
            self.res = left + right + 2
            return -1
        elif left >= 0 and right < 0:
            return left + 1
        elif left < 0 and right >= 0:
            return right + 1
        else:
            return -1
    
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        # find the LCA of p and q
        # use a variable to store the distances from current node to p or q
        self.res = 0
        self.helper(root, p, q)
        return self.res
