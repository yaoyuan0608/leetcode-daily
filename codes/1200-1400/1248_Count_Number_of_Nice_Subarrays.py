class Solution:
    from typing import List
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # subarray problem with exact k constrain
        def helper(maximum):
            left, right = 0, 0
            res = 0
            count = 0
            for right in range(len(nums)):
                if nums[right] %2 == 1:
                    count += 1
                while count > maximum and left <= right:
                    count -= nums[left]%2==1
                    left += 1
                res += right - left
            return res
        return helper(k) - helper(k-1)