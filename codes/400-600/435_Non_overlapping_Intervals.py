class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # in order to make all intervals non-overlapped, we can greedily search one by one
        # sort the intervals by start point
        # remove all intervals until its starting point is greater than the current end pivot
        # each time remove an interval, update the pivot as the smallest end point
        
        intervals = sorted(intervals, key=lambda x: x[0])
        pivot = intervals[0][1]
        count = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < pivot:
                count += 1
                pivot = min(pivot, intervals[i][1])
            else:
                pivot = intervals[i][1]
        return count