class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        # for a 0 subarray with length k, the total count will be sum(k)
        count = 0
        tmp = 0
        idx = 0
        tmp_idx = 0
        while idx < len(nums):
            if nums[idx] != 0:
                idx += 1
                tmp_idx = idx
            else:
                tmp_idx = idx
                while tmp_idx < len(nums) and nums[tmp_idx] == 0:
                    tmp_idx += 1
                    tmp += 1
                idx = tmp_idx
                count += tmp*(tmp+1)//2
                tmp = 0
        return count