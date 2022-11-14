class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        d = defaultdict(int)
        res = 0
        for num in nums:
            d[num%space] += 1
            res = max(res, d[num%space])
        output = float('inf')
        for num in nums:
            if d[num%space] == res:
                output = min(num, output)
        return output