class Solution:
    def get_sum(self, x):
        count = 0
        for string in str(x):
            count += int(string)
        return count
    def maximumSum(self, nums: List[int]) -> int:
        value_d = defaultdict(list)
        for index, num in enumerate(nums):
            count = self.get_sum(num)
            value_d[count].append(index)
        
        res = float('-inf')
        for key in value_d.keys():
            if len(value_d[key]) > 1:
                res = max(res, sum(sorted([nums[x] for x in value_d[key]], reverse=True)[:2]))
        if res > float('-inf'):
            return res
        else:
            return -1