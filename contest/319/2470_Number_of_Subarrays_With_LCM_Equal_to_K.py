class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        def LCM(a, b):
            return abs(a*b) // math.gcd(a, b)
        
        count = 0
        for i in range(len(nums)):
            curr_lcm = nums[i]
            for j in range(i, len(nums)):
                curr_lcm = LCM(curr_lcm, nums[j])
                if curr_lcm == k:
                    count += 1

        return count