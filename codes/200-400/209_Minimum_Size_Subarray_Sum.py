class Solution:
    from typing import List
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        res = len(nums)
        count = 0
        if sum(nums) < target:
            return 0
        for right in range(len(nums)):
            count += nums[right]
            while count >= target and left <= right:
                res = min(res, right-left+1)
                count -= nums[left]
                left += 1
        
        return res