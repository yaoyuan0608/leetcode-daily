class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if (grid[0][1] not in (0, 1) and grid[1][0] not in (0, 1)): 
            return -1
        m, n = len(grid), len(grid[0])
        visited = set()
        hq = [(grid[0][0], 0, 0)]
        
        while hq:
            time, row, col = heappop(hq)
            if row == m-1 and col == n-1: 
                return time
            if (row, col) in visited: 
                continue
            visited.add((row, col))
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                r, c = row + dr, col + dc
                if 0 <= r < m and 0 <= c < n and (r, c) not in visited:
                    if (grid[r][c] - time > 1 and (grid[r][c] - time) % 2 == 0):
                        f = 1
                    else:
                        f = 0
                    heappush(hq, (max(time + 1, grid[r][c] + f), r, c))
        return -1