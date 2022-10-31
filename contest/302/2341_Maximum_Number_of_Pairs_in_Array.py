class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        idx = 1
        pairs = 0
        while idx < len(nums):
            if nums[idx] == nums[idx-1]:
                pairs += 1
                idx += 2
            else:
                idx += 1
        return [pairs, len(nums) - 2*pairs]