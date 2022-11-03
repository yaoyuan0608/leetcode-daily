class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # similar to 340: Longest Substring with At Most K Distinct Characters
        # k replacement = sum of all different strings occurance
        from collections import defaultdict
        def count_diff(d):
            values = sorted(d.values())
            return sum(values[:-1])
        
        left, right = 0, 0
        res = 0
        seen = defaultdict(int)
        for right in range(len(s)):
            string = s[right]
            seen[string] += 1
            total_diff = count_diff(seen)
            while total_diff > k:
                old_string = s[left]
                seen[old_string] -= 1
                if seen[old_string] == 0:
                    del seen[old_string]
                left += 1
                total_diff = count_diff(seen)
            res = max(res, right - left + 1)
        return res