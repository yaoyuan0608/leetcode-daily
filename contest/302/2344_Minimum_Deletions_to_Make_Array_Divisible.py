class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        nums = sorted(nums)
        scd = reduce(gcd, numsDivide)
        count = 0
        for i in range(len(nums)):
            if scd%nums[i] == 0:
                return count
            elif nums[i] < scd:
                count += 1
            else:
                return -1
        return -1