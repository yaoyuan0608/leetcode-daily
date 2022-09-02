# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        # need to store the minimum diff and corresponding node
        diff = float('inf')
        res = -1
        
        while root:
            tmp_diff = root.val - target
            if abs(tmp_diff) < diff:
                res = root.val
                diff = abs(tmp_diff)
            if tmp_diff == 0:
                return res
            elif tmp_diff > 0:
                root = root.left
            else:
                root = root.right
        return res