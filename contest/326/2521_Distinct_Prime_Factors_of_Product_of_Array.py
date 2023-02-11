class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        res = []
        for i in range(len(nums)):
            if nums[i] == 2:
                res.append(nums[i])
            else:
                sq = int(math.sqrt(nums[i]))
                for j in range(2, sq + 1):
                    if nums[i] % j == 0:
                        res.append(j)
                        while (nums[i] % j == 0) :
                            nums[i] //= j
            if (nums[i] > 2) :
                res.append(nums[i])
        return len(set(res))