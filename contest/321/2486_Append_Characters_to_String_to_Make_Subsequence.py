class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        p1, p2 = 0, 0
        # find the longest common subsequence first
        while p1 < len(s) and p2 < len(t):
            if s[p1] == t[p2]:
                p1 += 1
                p2 += 1
            else:
                p1 += 1
                
        return len(t) - p2