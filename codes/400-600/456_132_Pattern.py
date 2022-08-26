class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # find the minimum value of each element on its left side
        # scan from right to left, at a certain point, 
        # if its lefmost minimum is smaller than current maximum, return True
        if len(nums) < 3:
            return False
        minimum = [float('inf')] * len(nums)
        minimum[1] = nums[0]
        for i in range(2, len(nums)):
            minimum[i] = min(minimum[i-1], nums[i-1])
        
        # maitain a decreasing monotonic stack, so that the current maximum is rightmost maximum
        # greedy strategy that compare the minimum on left side(i), and ensure it is the rightmost maximum(j)
        # then we only need to compare i and k
        stack = []
        for i in range(len(nums)-1, -1, -1):
            tmp_max = float('-inf')
            while stack and nums[stack[-1]] < nums[i]:
                idx = stack.pop()
                tmp_max = max(tmp_max, nums[idx])
            if tmp_max > minimum[i]:
                return True
            stack.append(i)
        return False