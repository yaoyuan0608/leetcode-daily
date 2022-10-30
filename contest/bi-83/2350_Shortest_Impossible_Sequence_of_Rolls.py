class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        # an array with length n contains at most k number. find out the smallest sequence that is not shown in the array
        # sequence comes from the combination of k
        tmp_set = set()
        res = 1
        for roll in rolls:
            tmp_set.add(roll)
            if len(tmp_set) == k:
                tmp_set = set()
                res += 1
        return res