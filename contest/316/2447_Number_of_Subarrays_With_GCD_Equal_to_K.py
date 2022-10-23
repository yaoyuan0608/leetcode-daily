class Solution:
    import math
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            # for each i, do a for loop till the end
            curr_gcd = nums[i]
            for j in range(i, len(nums)):
                # if current gcd is smaller than k, break it
                curr_gcd = math.gcd(curr_gcd, nums[j])
                if curr_gcd == k:
                    count += 1
                elif curr_gcd < k:
                    break
        return count