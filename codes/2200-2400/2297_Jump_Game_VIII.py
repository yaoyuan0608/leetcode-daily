class Solution:
    def minCost(self, nums: List[int], costs: List[int]) -> int:
        # use monotonic stack to find the next greater/smaller element, which is the moving candidate.
        # given all possible states, use dp to find the minimum cost
        costs[0] = 0

        stack_inc = []
        stack_dec = []
        next_greater = [len(nums)] * len(nums)
        next_smaller = [len(nums)] * len(nums)
        for idx in range(len(nums)):
            while stack_inc and nums[idx] >= nums[stack_inc[-1]]:
                tmp = stack_inc.pop()
                next_greater[tmp] = idx
            while stack_dec and nums[idx] < nums[stack_dec[-1]]:
                tmp = stack_dec.pop()
                next_smaller[tmp] = idx

            stack_inc.append(idx)
            stack_dec.append(idx)
        
        def dp(x):
            if x in memo:
                return memo[x]
            if x == len(nums):
                memo[x] = float('inf')
                return float('inf')
            if x == len(nums)-1:
                memo[x] = costs[-1]
                return costs[-1]
            cost = costs[x]
            cost += min(dp(next_greater[x]), dp(next_smaller[x]))
            memo[x] = cost
            return cost

        memo = {}
        return dp(0)