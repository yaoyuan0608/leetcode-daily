class Solution:
    from typing import List
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # find the windows whose sum is exactly equal to goal
        # = find the sum at most goal - find the sum at most (goal-1)
        def helper(goal):
            left, right = 0, 0
            count = 0
            res = 0
            for right in range(len(nums)):
                count += nums[right]
                while count > goal and left <= right:
                    count -= nums[left]
                    left += 1
                if left <= right:
                    res += right - left + 1
            return res
        return helper(goal) - helper(goal-1)