class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # greedy, consider the longest index we can reach at each idx
        maximum = 0
        for idx, num in enumerate(nums):
            if maximum >= len(nums) - 1:
                return True
            if maximum < idx:
                return False
            maximum = max(maximum, idx + num)
        return False