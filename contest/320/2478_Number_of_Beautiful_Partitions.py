class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        if s[0] not in ['2','3','5','7'] or s[-1] in ['2','3','5','7']:
            return 0
    
        prime = set(['2','3','5','7'])
        MOD = 1000000007
        split = []
        memo = {}
        for i in range(minLength-1, len(s)-minLength):
            if s[i] not in prime and s[i+1] in prime:
                split.append(i)
        
        def dp(idx, k_):
            if (idx, k_) in memo:
                return memo[(idx, k_)]
            if k_ == k-1:
                memo[(idx, k_)] = 1
                return 1
            if idx >= len(split):
                memo[(idx, k_)] = 0
                return 0
            # not enough split after
            if k_ + len(split) - idx < k - 1: 
                memo[(idx, k_)] = 0
                return 0
            count = 0
            # skip current split index
            count = (count + dp(idx+1, k_)) % MOD
            # find choose current split index and start from the next available index
            most_left = bisect_left(split, split[idx] + minLength)
            count = (count + dp(most_left, k_+1)) % MOD
            memo[(idx, k_)] = count
            return count
        
        return dp(0, 0)