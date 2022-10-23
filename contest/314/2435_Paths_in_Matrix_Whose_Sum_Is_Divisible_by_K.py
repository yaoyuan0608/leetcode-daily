class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        dp = [[[0] * k for _ in range(len(grid[0]))] for _ in range(len(grid))]
        total = grid[0][0]
        dp[0][0][total%k] = 1
        for i in range(1,len(grid)):
            val = grid[i][0] % k
            for m in range(k):
                dp[i][0][(val+m)%k] += dp[i-1][0][m]

        total = grid[0][0]
        for j in range(1,len(grid[0])):
            val = grid[0][j] % k
            for m in range(k):
                dp[0][j][(val+m)%k] += dp[0][j-1][m]

        total = grid[0][0] 
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                val = grid[i][j] % k
                for m in range(k):
                    dp[i][j][(val+m)%k] = (dp[i][j][(val+m)%k]+dp[i-1][j][m] + dp[i][j-1][m]) % 1000000007
        

        return dp[-1][-1][0]