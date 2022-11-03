class Solution:
    from typing import List
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        res = 0
        count = 1
        for right in range(len(nums)):
            count *= nums[right]
            while count >= k and left <= right:
                old = nums[left]
                count //= old
                left += 1
            res += right - left + 1
        return res