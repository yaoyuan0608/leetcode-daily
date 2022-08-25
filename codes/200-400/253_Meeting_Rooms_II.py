class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # greedy problem
        # sort the intervals by starting point, use a pivot ending point
        # when the next interval comes in, update the room number if its starting point is smaller than pivot
        # use a heap to store current the ending points of room in used
        
        intervals = sorted(intervals, key=lambda x: x[0])
        count = 1
        hq = []
        hq.append(intervals[0][1])
        for i in range(1, len(intervals)):
            # current smallest ending point is smaller, empty it
            if hq[0] <= intervals[i][0]:
                heapq.heappop(hq)
            else:
                count += 1
            heapq.heappush(hq, intervals[i][1])
        return count