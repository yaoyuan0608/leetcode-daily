class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        # classical dp problem, find the longest path with some constraints
        # dp[i] = max(dp[i], dp[j]+1), for j in [i,i+d]/[i-d,i] and arr[j] < arr[i]
        memo = {}
        def dp(i):
            if i in memo:
                return memo[i]
            res = 1
            for j in range(i+1, i+d+1):
                if (not 0 <= j < len(arr)) or arr[j] >= arr[i]:
                    break
                res = max(res, dp(j) + 1)
            for j in range(i-1, i-d-1, -1):
                # constraints
                if (not 0 <= j < len(arr)) or arr[j] >= arr[i]:
                    break
                res = max(res, dp(j) + 1)
            memo[i] = res
            return res
        output = 1
        for i in range(len(arr)):
            output = max(output, dp(i))
        return output