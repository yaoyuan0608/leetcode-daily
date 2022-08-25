class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # greedy problem
        # sort the intervals by starting point, create a pivot ending point
        # update pivot point when iterating the intervals
        # when the current starting point is larger than the pivot point, create a new interval
        
        res = []
        intervals = sorted(intervals, key=lambda x: x[0])
        res.append(intervals[0])
        
        for i in range(1, len(intervals)):
            if intervals[i][0] <= res[-1][1]:
                res[-1] = [res[-1][0], max(res[-1][1], intervals[i][1])]
            else:
                res.append(intervals[i])
        return res