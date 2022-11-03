class Solution:
    from typing import List
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # at certain idx, the maximum possible freq will be the smallest i, such that sum(nums[i:idx+1]) + k >= nums[idx] * (idx - i + 1)
        nums = sorted(nums)
        left, right = 0, 0
        res = 0
        count = 0
        for right in range(len(nums)):
            biggest = nums[right]
            count += biggest
            while count + k < biggest * (right - left + 1) and right >= left:
                smallest = nums[left]
                count -= smallest
                left += 1
            res = max(res, right - left + 1)
        return res