class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        raw = list(Counter(nums).values())
        counter = []
        counter.append(raw[0])
        for i in range(1, len(raw)):
            counter.append(counter[-1] + raw[i])
        
        res = 0
        for i in range(1, len(counter)):
            # the possible triplets on each index: left * mid * right
            # val1: left sum, val2: right sum, val3: current index
            val1 = counter[i-1]
            val2 = counter[-1] - counter[i]
            val3 = counter[i] - counter[i-1]
            res += val1 * val2 * val3
        return res