class Solution:
    def findCrossingTime(self, n: int, k: int, time: List[List[int]]) -> int:
        # maintain four hq
        # ll: cross bridge from left to right, rr: cross from right to left
        res, count = 0, 0
        l, ll = [], []
        r, rr = [], []
        for i, (x, _, y, _) in enumerate(time):
            heapq.heappush(ll, (-x-y, -i))
        
        # end states
        while n or r or rr:
            # cand: the next available time
            if not rr and (not r or r[0][0] > count) and (not n or not ll and (not l or l[0][0] > count)): 
                cand = float('inf')
                if n and l:
                    cand = min(cand, l[0][0])
                if r:
                    cand = min(cand, r[0][0])
                count = cand
            # while any candidate can be pushed into rr/ll
            while r and r[0][0] <= count: 
                _, i = heapq.heappop(r)
                heapq.heappush(rr, (-time[i][0] - time[i][2], -i))
            while l and l[0][0] <= count: 
                _, i = heapq.heappop(l)
                heapq.heappush(ll, (-time[i][0] - time[i][2], -i))
            if rr: 
                _, i = heapq.heappop(rr)
                count += time[-i][2]
                if n: 
                    heapq.heappush(l, (count + time[-i][3], -i))
                else: 
                    res = max(res, count)
            else: 
                _, i = heapq.heappop(ll)
                count += time[-i][0]
                heapq.heappush(r, (count + time[-i][1], -i))
                n -= 1
        return res