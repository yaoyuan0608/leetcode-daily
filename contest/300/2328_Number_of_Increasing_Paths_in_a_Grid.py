class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        # dp[i][j]: number of paths starting from (i,j)
        # dp[i][j] += dp[i+-1][j+-1]
        memo = {}
        MOD = 1000000007
        def dp(i, j):
            if (i,j) in memo:
                return memo[(i,j)]
            count = 1
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                x = dx+i
                y = dy+j
                if 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y] > grid[i][j]:
                    count = (count + dp(x,y)) % MOD
            memo[(i,j)] = count
            return count
        
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res = (res + dp(i,j)) % MOD
        return res