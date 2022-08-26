class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # in order to find the next greater element, maintain a decreasing monotonic stack
        # pop the idx from stack, so that at these idxes, the values are smaller than the pivot point
        new_nums = nums + nums
        stack = []
        res = [-1] * len(new_nums)
        for i in range(0, len(new_nums)):
            cur_num = new_nums[i]
            while stack and new_nums[stack[-1]] < cur_num:
                idx = stack.pop()
                res[idx] = cur_num
            stack.append(i)
        return res[:len(nums)]