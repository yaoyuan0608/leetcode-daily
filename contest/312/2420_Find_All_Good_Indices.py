class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        # use two list to store the non-increasing index and non-decreasing index
        # prefix[i] represents the longest length before i
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)
        
        for idx in range(1, len(nums)):
            if idx == 1:
                prefix[idx] = 1
            elif nums[idx-1] <= nums[idx-2]:
                prefix[idx] = prefix[idx-1] + 1
            else:
                prefix[idx] = 1
        
        for idx in range(len(nums)-2, -1, -1):
            if idx == len(nums)-2:
                suffix[idx] = 1
            elif nums[idx+1] <= nums[idx+2]:
                suffix[idx] = suffix[idx+1] + 1
            else:
                suffix[idx] = 1
        res = []
        #print(prefix, suffix)
        for i in range(1,len(nums)-1):
            if prefix[i] >= k and suffix[i] >= k:
                res.append(i)
        return res