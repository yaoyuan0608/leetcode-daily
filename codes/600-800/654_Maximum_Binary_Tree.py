# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, nums):
        max_val = max(nums)
        idx = nums.index(max_val)
        left_nums, right_nums = nums[:idx], nums[idx+1:]
        root = TreeNode(max_val)
        if left_nums:
            root.left = self.helper(left_nums)
        if right_nums:
            root.right = self.helper(right_nums)
        return root
    
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        # find the maximum and set it as root, do it recursively
        return self.helper(nums)