class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        if k < 10:
            single = list(set(s))
            for s_ in single:
                if int(s_) > k:
                    return -1
        start = 0
        end = 0
        count = 0
        res = []
        while end < len(s):
            cur_num = s[start:end+1]
            if int(cur_num) <= k:
                end += 1
            else:
                res.append(s[start:end])
                start = end
                end = start
                count += 1
                
        return count+1