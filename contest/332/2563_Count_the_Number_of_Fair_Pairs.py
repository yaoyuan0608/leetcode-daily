class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums = sorted(nums)
        dp1 = [0] * len(nums)
        dp2 = [0] * len(nums)
        l, r = 0, len(nums)-1
        while l <= r:
            # most left boundary 
            if nums[l] + nums[r] >= lower:
                dp1[r] = l
                r -= 1
            # most right boundary
            else:
                dp1[l] = r+1
                l += 1
        l, r = 0, len(nums)-1
        while l <= r:
            if nums[l] + nums[r] <= upper:
                dp2[l] = r
                l += 1
            else:
                dp2[r] = l-1
                r -= 1
        #print(dp1, dp2)
        count = 0
        for index, (val1, val2) in enumerate(zip(dp1, dp2)):
            count += val2 - val1 + 1 - (val1<=index<=val2)
        return count // 2