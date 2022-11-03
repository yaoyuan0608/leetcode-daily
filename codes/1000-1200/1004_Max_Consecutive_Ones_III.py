class Solution:
    from typing import List
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        res = 0
        count = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                count += 1
            while count > k:
                count -= (nums[left] == 0)
                left += 1
            res = max(res, right - left + 1)
        return res