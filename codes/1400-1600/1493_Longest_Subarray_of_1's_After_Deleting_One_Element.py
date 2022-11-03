class Solution:
    from typing import List
    def longestSubarray(self, nums: List[int]) -> int:
        # maintain a sliding window in which at most one zero
        left, right = 0, 0
        count = 0
        res = 0
        for right in range(len(nums)):
            count += nums[right] == 0
            if count > 1 and left <= right:
                count -= nums[left] == 0
                left += 1
            # no need to +1, bc we need to delete one number
            res = max(res, right - left)
        return res