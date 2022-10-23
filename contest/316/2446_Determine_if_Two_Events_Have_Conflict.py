class Solution:
    def convert(self, string):
        hour, minute = string.split(':')
        return int(hour) + int(minute)/60
    
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        # similar to non-overlapping problem, we just need to compare whether two intervals have intersection.
        start1, end1 = event1
        start2, end2 = event2
        start1, end1 = self.convert(start1), self.convert(end1)
        start2, end2 = self.convert(start2), self.convert(end2)
        
        if end1 < start2 or end2 < start1:
            return False
        else:
            return True