class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        # use two stacks, stack2 is used to store the index whose second greater value not occur
        # stack1 is used to store the index whose first greater value not occer
        # when a new num comes, check stack2 first, pop out all values smaller than num
        # check stack1 after, pop out all values smaller than num and append it to stack2
        res = [-1] * len(nums)
        stack1 = []
        stack2 = []
        for index, num in enumerate(nums):
            while stack2 and nums[stack2[-1]] < num:
                res[stack2.pop()] = num
            tmp = []
            while stack1 and nums[stack1[-1]] < num:
                tmp.append(stack1.pop())
            stack2 += tmp[::-1]
            stack1.append(index)
        return res