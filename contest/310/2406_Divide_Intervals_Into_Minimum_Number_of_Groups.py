class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x:(x[0]))
        count = 1
        hq = []
        hq.append(intervals[0][1])
        for i in range(1, len(intervals)):
            # current smallest ending point is smaller, empty it
            if hq[0] < intervals[i][0]:
                heapq.heappop(hq)
            else:
                count += 1
            heapq.heappush(hq, intervals[i][1])
        return count