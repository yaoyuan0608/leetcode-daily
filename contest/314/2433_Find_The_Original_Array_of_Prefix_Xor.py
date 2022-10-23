class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        res = [pref[0]]
        if len(pref) == 1:
            return res
        for i in range(1, len(pref)):
            res.append(pref[i-1] ^ pref[i])
        return res