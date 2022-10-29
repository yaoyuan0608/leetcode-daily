class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        # define initial states, default array is nums[0] with lenght 1
        res = 1
        length = 1
        start = 0
        nxt = 1
        count = nums[0]
        
        while nxt < len(nums):
            if nums[nxt] & count == 0:
                length += 1
                res = max(res, length)
                count += nums[nxt]
                nxt += 1
            else:
                while start < nxt and nums[nxt] & count != 0:
                    count -= nums[start]
                    length -= 1
                    start += 1
            
        return res