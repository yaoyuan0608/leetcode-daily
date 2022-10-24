class Solution:
    def partitionString(self, s: str) -> int:
        # sliding window
        count = 0
        seen = set()
        for string in s:
            if string not in seen:
                seen.add(string)
            else:
                count += 1
                seen = set()
                seen.add(string)
        return count+1