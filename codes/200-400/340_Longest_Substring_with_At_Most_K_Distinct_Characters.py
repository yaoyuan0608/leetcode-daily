class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        from collections import defaultdict
        # shirnkable sliding windows to solve at-most problem
        left, right = 0, 0
        res = 0
        seen = defaultdict(int)
        for right in range(len(s)):
            string = s[right]
            seen[string] += 1
            # when more than k characters exist
            while len(seen) > k:
                old_string = s[left]
                seen[old_string] -= 1
                if seen[old_string] == 0:
                    del seen[old_string]
                left += 1
            res = max(res, right - left + 1)
        return res