class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        # dp[i] = max(dp[i], nums[i] + dp[k]), for k in [i-k, i-1]
        # use a heap to store the current maximum value in [i-k, i-1]
        dp = [0] * len(nums)
        hq = []
        for i in range(len(nums)):
            # lazy pop out
            while hq and hq[0][1] < i-k:
                heapq.heappop(hq)
            if i == 0:
                dp[i] = nums[i]
            else:
                idx = hq[0][1]
                dp[i] = dp[idx] + nums[i]
            heapq.heappush(hq, (-dp[i], i))
        return dp[-1]