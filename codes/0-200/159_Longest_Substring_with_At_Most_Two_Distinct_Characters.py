class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        from collections import defaultdict
        # shrinkable sliding windows
        left, right = 0, 0
        res = 0
        seen = defaultdict(int)
        for right in range(len(s)):
            string = s[right]
            seen[string] += 1
            # if more than two characters exists
            while len(seen) > 2:
                old_string = s[left]
                seen[old_string] -= 1
                if seen[old_string] == 0:
                    del seen[old_string]
                left += 1
            res = max(res, right - left + 1)
        return res