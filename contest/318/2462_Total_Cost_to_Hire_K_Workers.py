class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        if candidates * 2 >= len(costs):
            return sum(sorted(costs)[:k])
        
        left = 0
        right = len(costs) - 1
        mid = len(costs)//2+1
        hq = []
        #print(len(costs))
        for _ in range(candidates):
            heapq.heappush(hq, (costs[left], 'l'))
            left += 1
            heapq.heappush(hq, (costs[right], 'r'))
            right -= 1

        res = 0
        count = 0
        for _ in range(k):
            minimum, idx = heapq.heappop(hq)
            res += minimum
            count += 1
            #print(left, right, res, minimum, idx, hq)
            if left > right:
                remain = k - count
                for _ in range(remain):
                    res += heapq.heappop(hq)[0]
                return res
            
            if idx == 'l':
                heapq.heappush(hq, (costs[left], 'l'))
                left += 1
            else:
                heapq.heappush(hq, (costs[right], 'r'))
                right -= 1
        return res