class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def isValid(x):
            # dp0: no rob current, dp1: rob current
            dp0, dp1 = 0, 0
            for num in nums:
                if num <= x:
                    dp0,dp1 = max(dp0, dp1), dp0+1
                else:
                    dp0,dp1 = max(dp0,dp1), 0
            return max(dp0, dp1) >= k
        
        l, r = 1, max(nums)+1
        while l < r:
            mid = l + (r-l) // 2
            if isValid(mid):
                r = mid
            else:
                l = mid + 1
        return l
        