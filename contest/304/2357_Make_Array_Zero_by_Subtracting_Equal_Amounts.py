class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        nums = [x for x in nums if x != 0]
        while sum(nums) != 0:
            sub = min(nums)
            new_nums = []
            for x in nums:
                if x != 0:
                    x -= sub
                if x != 0:
                    new_nums.append(x)
            nums = new_nums
            count += 1
        return count