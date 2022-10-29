class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        diff = []
        for idx, val in enumerate(nums):
            diff.append(val-idx)
        
        diff_d = defaultdict(int)
        for dif in diff:
            diff_d[dif] += 1
        count = 0
        #print(diff_d)
        n = len(nums)
        for key, value in diff_d.items():
            count += value*(n-value)
        
        return count // 2