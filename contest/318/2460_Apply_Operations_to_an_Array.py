class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                res.append(nums[i] * 2)
                nums[i+1] = 0
            else:
                res.append(nums[i])
        res.append(nums[-1])
        new_res = []
        for i in range(len(res)):
            if res[i] != 0:
                new_res.append(res[i])
        new_res += [0] * (len(res) - len(new_res))
        return new_res