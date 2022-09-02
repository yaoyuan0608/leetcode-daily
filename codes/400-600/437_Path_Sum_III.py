# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node, val):
        if not node:
            return
        val += node.val
        if val - self.target in self.map:
            self.count += self.map[val-self.target]
        if val in self.map:
            self.map[val] += 1
        else:
            self.map[val] = 1
        self.helper(node.left, val)
        self.helper(node.right, val)
        # reduce by 1 because we wont go back the same path again
        self.map[val] -= 1
        
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # recursive from root, problem like 2-sum
        self.map = {0:1}
        self.count = 0
        self.target = targetSum
        self.helper(root, 0)
        print(self.map)
        return self.count