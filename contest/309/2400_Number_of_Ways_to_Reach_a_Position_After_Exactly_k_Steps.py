class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        memo = {}
        MOD = 1000000007
        def dp(step, pos):
            if step == 0:
                if pos == endPos:
                    memo[(step, pos)] = 1
                    return 1
                else:
                    memo[(step, pos)] = 0
                    return 0
            if (step, pos) in memo:
                return memo[(step, pos)]

            count = (dp(step-1, pos+1) + dp(step-1, pos-1)) % MOD
            memo[(step, pos)] = count
            return count
        
        return dp(k, startPos)