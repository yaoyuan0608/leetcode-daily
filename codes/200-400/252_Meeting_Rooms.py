class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # An intuitive thinking is check whether there are any overlap on these intervals
        
        if not intervals:
            return True
        intervals = sorted(intervals, key=lambda x: x[0])
        pivot = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < pivot:
                return False
            else:
                pivot = intervals[i][1]
        return True