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
        self.stack.append(node.val)
        self.helper(node.right)
        
    def bsearh_upper(self, target):
        left = 0
        right = len(self.stack)
        while left < right:
            mid = left + (right-left) // 2
            if self.stack[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left
    
    def bsearch_lower(self, target):
        left = 0
        right = len(self.stack)
        while left < right:
            mid = left + (right-left)//2
            if not self.stack[mid] <= target:
                right = mid
            else:
                left = mid + 1
        return left - 1
    
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        self.stack = []
        self.helper(root)
        # flatten the tree inorder
        res = []
        minimum, maximum = -1, -1
        # find the maximum smaller value and minimum bigger value
        for idx, q in enumerate(queries):
            right, left = self.bsearh_upper(q), self.bsearch_lower(q)
            if left < len(self.stack) and self.stack[left] <= q:
                lower = self.stack[left]
            else:
                lower = -1
            
            if right >=0 and right < len(self.stack) and self.stack[right] >= q:
                upper = self.stack[right]
            else:
                upper = -1
            res.append([lower,upper])
        return res