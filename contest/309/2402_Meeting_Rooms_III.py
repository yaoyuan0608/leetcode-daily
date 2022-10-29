class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # simulation, use a heap to store the current meeting, and keep the size to n
        # use a list to store the number of meetings per room
        hp = []
        count = [0] * n
        free = 0
        meetings = sorted(meetings,key=lambda x:x[0])
        not_aval = set()
        for start, end in meetings:
            # pop out all finished meeting
            while free in not_aval:
                free += 1
                
            while hp and hp[0][0] <= start:
                last_end, room = heapq.heappop(hp)
                free = min(free, room)
                not_aval.remove(room)
                
            if len(hp) < n:
                count[free] += 1
                heapq.heappush(hp, (end, free))
                not_aval.add(free)
                free += 1
                
            else:
                last_end, room = heapq.heappop(hp)
                free = min(free, room)
                not_aval.remove(room)
                diff = last_end - start
                count[free] += 1
                heapq.heappush(hp, (end+diff, room))
                not_aval.add(free)
                free += 1
                
        maximum = float('-inf')
        res = -1
        for idx, value in enumerate(count):
            if value > maximum:
                res = idx
                maximum = value
        return res