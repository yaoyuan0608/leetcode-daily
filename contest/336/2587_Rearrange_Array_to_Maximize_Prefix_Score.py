class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums = sorted(nums, reverse=True)
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])
        
        count = 0
        for p in prefix:
            if p > 0:
                count += 1
        return count