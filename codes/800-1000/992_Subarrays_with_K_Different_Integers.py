class Solution:
    from typing import List
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        def helper(val):
            left, right = 0, 0
            count = 0
            res = 0
            seen = defaultdict(int)
            for right in range(len(nums)):
                num = nums[right]
                seen[num] += 1
                while len(seen) > val:
                    old = nums[left]
                    seen[old] -= 1
                    if seen[old] == 0:
                        del seen[old]
                    left += 1
                res += right-left + 1
            return res
        
        return helper(k) - helper(k-1)