class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        left, right = 0, 0
        res = s
        count = len(t)
        flag = float('inf')
        seen = Counter(t)
        
        for right in range(len(s)):
            string = s[right]
            if string in seen:
                if seen[string] > 0:
                    count -= 1
                seen[string] -= 1
            # if count == 0, we meet the requirement
            while count == 0:
                if right - left + 1 <= len(res):
                    res = s[left:right+1]
                    flag = right-left+1
                old = s[left]
                if old in seen:
                    seen[old] += 1
                    if seen[old] > 0:
                        count += 1
                left += 1
        if flag < float('inf'):
            return res
        else:
            return ''