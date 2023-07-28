class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        q = deque()
        seen = set()
        res = 0
        for i in range(len(grid)):
            q.append((i,0,0))
        while q:
            for _ in range(len(q)):
                x,y,length = q.popleft()
                if (x,y) in seen:
                    continue
                seen.add((x,y))
                res = max(res, length)
                for dx, dy in [(-1,1),(0,1),(1,1)]:
                    xx = x+dx
                    yy = y+dy
                    if 0<=xx<len(grid) and 0<=yy<len(grid[0]) and grid[xx][yy] > grid[x][y]:
                        q.append((xx,yy,length+1))
        return res