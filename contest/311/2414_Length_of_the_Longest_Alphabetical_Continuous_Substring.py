class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        # sliding windows
        if not s:
            return 0
        res = 1
        count = 1
        prev = s[0]
        for string in s[1:]:
            if ord(string) - ord(prev) == 1:
                count += 1
                res = max(res, count)
                prev = string
            else:
                count = 1
                prev = string
        return res