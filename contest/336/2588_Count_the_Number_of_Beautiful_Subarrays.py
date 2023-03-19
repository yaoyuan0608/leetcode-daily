class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        # find all subarray in which nums[i]^..^nums[j] = 0
        # two sum problem
        value_dict = {0:1}
        prefix = 0
        count = 0
        for num in nums:
            prefix ^= num
            if prefix in value_dict:
                #print(prefix, num)
                count += value_dict[prefix]
                value_dict[prefix] += 1
            else:
                value_dict[prefix] = 1
        return count