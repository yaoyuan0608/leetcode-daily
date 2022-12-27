class Solution:
    def jump(self, nums: List[int]) -> int:
        # at each step, find the longest possible index
        if len(nums) <= 1:
            return 0
        start = 0
        end = start + nums[start]
        count = 1
        while end < len(nums)-1:
            count += 1
            longest = end
            # once we find the longest index, we can set it as the next ending point for next step
            for j in range(start, end+1):
                longest = max(longest, nums[j] + j)
            start, end = end, longest
        return count