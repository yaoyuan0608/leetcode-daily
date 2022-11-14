class Solution:
    def averageValue(self, nums: List[int]) -> int:
        count = 0
        total = 0
        for num in nums:
            if num%6 == 0:
                total += num
                count += 1
        if count == 0:
            return 0
        else:
            return math.floor(total/count)