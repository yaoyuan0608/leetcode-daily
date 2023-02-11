class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        counter1 = Counter(basket1)
        for x in basket2: 
            counter1[x] -= 1
        
        last = []
        for k, v in counter1.items():
            if v % 2 != 0:
                return -1
            last += [k] * abs(v // 2)
        
        minimum = min(basket1 + basket2)
        last = sorted(last)
        res = 0
        for i in range(len(last) // 2):
            res += min(2 * minimum, last[i])
        return res