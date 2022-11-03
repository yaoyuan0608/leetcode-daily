class Solution:
    from typing import List
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        from collections import defaultdict
        # sliding windows, maximum score with contrain
        left, right = 0, 0
        res = 0
        count = 0
        seen = defaultdict(int)
        for right in range(len(nums)):
            num = nums[right]
            count += num
            seen[num] += 1
            while len(seen) < right-left+1:
                old = nums[left]
                seen[old] -= 1
                if seen[old] == 0:
                    del seen[old]
                left += 1
                count -= old
            res = max(res, count)
        return res