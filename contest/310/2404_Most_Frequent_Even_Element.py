class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        freq_d = defaultdict(int)
        for num in nums:
            if num % 2 == 0:
                freq_d[num] += 1
        
        max_freq = float('-inf')
        for key,value in freq_d.items():
            if value >= max_freq:
                max_freq = value
        res = float('inf')
        for key, value in freq_d.items():
            if value == max_freq:
                res = min(res, key)
        if res < float('inf'):
            return res
        else:
            return -1