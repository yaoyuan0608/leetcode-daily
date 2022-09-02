# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, left: int, right: int):
            if left >= right:
                return [None]
            res = []
            for i in range(left, right):
                for tmp_l in self.helper(left, i):
                    for tmp_r in self.helper(i+1, right):
                        node = TreeNode(i)
                        node.left = tmp_l
                        node.right = tmp_r
                        res.append(node)
            return res
        
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        # start from each node, do backtrack
        return self.helper(1, n+1)