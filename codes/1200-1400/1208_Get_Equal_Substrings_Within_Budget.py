class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        # maximum substring length with constrain, sliding window problem
        left, right = 0, 0
        count = 0
        res = 0
        
        diff = []
        for s_, t_ in zip(s,t):
            val = abs(ord(s_) - ord(t_))
            diff.append(val)
        
        for right in range(len(diff)):
            count += diff[right]
            while count > maxCost:
                count -= diff[left]
                left += 1
            res = max(res, right - left + 1)
        return res