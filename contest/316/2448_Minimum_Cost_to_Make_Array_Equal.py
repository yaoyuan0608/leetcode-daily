class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        # when the costs for all nums are the same, then the desired point is the median
        # similarly, we can repeat each num with its cost time, and find the median
        new_nums = sorted(zip(nums, cost))
        total = sum(cost)
        curr = 0
        for index, (num, c) in enumerate(new_nums):
            curr += c
            if curr >= total / 2:
                median = num
                break
                
        count = 0
        for index, num in enumerate(nums):
            count += cost[index] * abs(num - median)
        return count