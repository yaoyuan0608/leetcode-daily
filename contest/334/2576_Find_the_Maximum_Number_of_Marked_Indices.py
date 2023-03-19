class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums = sorted(nums)
        count = 0
        idx1, idx2 = 0, (len(nums)+1) // 2
        while idx2 < len(nums):
            if nums[idx1] * 2 <= nums[idx2]:
                idx1 += 1
            idx2 += 1
        return idx1 * 2