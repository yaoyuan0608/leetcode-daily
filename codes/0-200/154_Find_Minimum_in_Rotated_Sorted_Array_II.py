class Solution:
    def findMin(self, nums: List[int]) -> int:
        # similar to problem 153
        l = 0
        r = len(nums) - 1
        while l < r:
            m = l + (r - l)//2
            # as there is duplicate values, it is possible that nums[m] == nums[r] but [m,r] is not sorted
            if nums[m] < nums[r]:
                r = m
            elif nums[m] > nums[r]:
                l = m+1
            # eliminate the duplicated impacts
            else:
                r -= 1
        return nums[l]