class Solution:
    from typing import List
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # sliding windows problem
        left, right = 0,0 
        res = 0
        count = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                count += 1
            while count > 1:
                old = nums[left]
                if old == 0:
                    count -= 1
                left += 1
            res = max(res, right - left + 1)
        return res