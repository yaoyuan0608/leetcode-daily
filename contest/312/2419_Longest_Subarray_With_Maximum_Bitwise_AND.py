class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        target = max(nums)
        res = 0
        start = 0
        idx = 0
        # two pointers, find the longest array such that all values are the same
        while idx < len(nums):
            if nums[idx] == target:
                start = idx
                while start < len(nums) and nums[start] == target:
                    res = max(res, start - idx + 1)
                    start += 1
                idx = start
            else:
                idx += 1
        return res