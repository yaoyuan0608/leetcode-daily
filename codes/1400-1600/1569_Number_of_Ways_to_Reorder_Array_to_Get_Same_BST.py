class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
class Solution:
    def helper(self, nums_list):
        root_val = nums_list[0]
        root = Node(root_val)
        left_nums, right_nums = [], []
        for x in nums_list[1:]:
            if x > root_val:
                right_nums.append(x)
            else:
                left_nums.append(x)
        if left_nums:
            root.left = self.helper(left_nums)
        if right_nums:
            root.right = self.helper(right_nums)
        
        return root
    
    def dp(self, node):
        # postorder dp, the result is the combination of size of left and right tree
        if not node:
            return 0
        if not node.left and not node.right:
            return 1
        left = self.dp(node.left)
        right = self.dp(node.right)
        
        self.count = comb(left+right, left) * self.count % self.MOD
        
        return left + right + 1
    
    def numOfWays(self, nums: List[int]) -> int:
        # create the tree by nums first, then use dynamic programming
        root = self.helper(nums)
        self.MOD = 1000000007
        self.count = 1
        self.dp(root)
        
        return self.count-1
