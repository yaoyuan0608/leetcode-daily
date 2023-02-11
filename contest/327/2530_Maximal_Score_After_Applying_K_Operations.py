class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        hq = []
        for num in nums:
            heapq.heappush(hq, -num)
        
        total = 0
        for _ in range(k):
            val = heapq.heappop(hq)
            val = -val
            total += val
            new_val = math.ceil(val/3)
            heapq.heappush(hq, -new_val)
        return total