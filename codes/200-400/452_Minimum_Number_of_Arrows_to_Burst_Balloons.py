class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # greedy problem
        # sort the intervals by start point, use a new arrow if a starting point is larger than current pivot
        # update the pivot as the smallest ending point so far
        
        points = sorted(points,key=lambda x:x[0])
        count = 1
        pivot = points[0][1]
        for i in range(1, len(points)):
            start, end = points[i]
            if start > pivot:
                count += 1
                pivot = end
            else:
                pivot = min(pivot, end)
        return count