class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        left_sum = [0]
        for i in range(len(nums)-1):
            left_sum.append(left_sum[-1] + nums[i])
        right_sum = [0]
        for i in range(len(nums)-1,0,-1):
            right_sum.append(right_sum[-1] + nums[i])
        right_sum = right_sum[::-1]

        res = []
        for l,r in zip(left_sum, right_sum):
            res.append(abs(l-r))
        return res