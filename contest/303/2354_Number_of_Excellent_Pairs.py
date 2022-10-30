class Solution:

    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        new = []
        for num in set(nums):
            new.append(bin(num).count('1'))
        new = sorted(new)
        idx = len(new)-1
        ans = 0
        for i in range(len(new)):
            while idx >= 0 and new[idx] + new[i] >= k:
                idx -= 1
            ans += len(new) - idx - 1
        return ans