class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        res = float('inf')
        count = 0
        for i, d in enumerate(divisors):
            tmp_count = 0
            for num in nums:
                if num%d == 0:
                    tmp_count += 1
            #print(tmp_count, d)
            if tmp_count > count:
                count = tmp_count
                res = d
            elif tmp_count == count:
                res = min(res, d)
        return res