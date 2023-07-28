class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rows, cols = [0] * n, [0] * m
        q = [(1, 0, 0)] # (dist, x, y)
        while q:
            d, x, y = heapq.heappop(q)
            if x == m - 1 and y == n - 1:
                return d
            for xx in range(max(x + 1, rows[y]), min(x + grid[x][y] + 1, m)):
                heapq.heappush(q, (d + 1, xx, y))
            rows[y] = max(rows[y], min(x + grid[x][y] + 1, m))

            for yy in range(max(y + 1, cols[x]), min(y + grid[x][y] + 1, n)):
                heapq.heappush(q, (d + 1, x, yy))
            cols[x] = max(cols[x], min(y + grid[x][y] + 1, n))
        return -1
