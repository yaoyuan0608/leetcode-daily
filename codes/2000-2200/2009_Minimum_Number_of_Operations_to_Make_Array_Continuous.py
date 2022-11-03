class Solution:
    from typing import List
    def minOperations(self, nums: List[int]) -> int:
        # find the longest subarray such that maximum-minimum=length-1
        # then the answer becomes original_length - longest_length
        n = len(nums)
        nums = sorted(list(set(nums)))
        left, right = 0, 0
        res = 0
        count = 0
        for right in range(len(nums)):
            maximum = nums[right]
            minimum = nums[left]
            # if the gap between max and min is larger than what we have, shrink the window
            while minimum + n <= maximum:
                left += 1
                minimum = nums[left]
            res = max(res, right - left + 1)
        return n - res