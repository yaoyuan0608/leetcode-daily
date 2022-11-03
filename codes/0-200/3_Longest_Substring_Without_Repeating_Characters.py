# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         l, r = 0, 0
#         res = 0
#         seen = [0] * 128
#         dup = 0
#         for r in range(len(s)):
#             seen[ord(s[r]) - ord('a')] += 1
#             dup += (seen[ord(s[r]) - ord('a')] == 2)
#             if dup > 0:
#                 seen[ord(s[l]) - ord('a')] -= 1
#                 dup -= (seen[ord(s[l]) - ord('a')] == 1)
#                 l += 1
#             res = max(res, r-l+1)
#         return res

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        res = 0
        # input contains alphabet and punctuation
        seen = [0] * 128
        for r in range(len(s)):
            seen[ord(s[r]) - ord('a')] += 1
            # if duplicate exists
            while seen[ord(s[r]) - ord('a')] > 1:
                seen[ord(s[l]) - ord('a')] -= 1
                l += 1
            res = max(res, r-l+1)
        return res