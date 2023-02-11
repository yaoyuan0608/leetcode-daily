class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts_sorted = []
        for g in gifts:
            heapq.heappush(gifts_sorted, -g)
            
        while k:
            selected = -heapq.heappop(gifts_sorted)
            selected = math.floor(math.sqrt(selected))
            heapq.heappush(gifts_sorted, -selected)
            k -= 1
        return -sum(gifts_sorted)