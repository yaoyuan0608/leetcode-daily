class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        count = 0
        prev = nums[-1]
        nums = nums[::-1]
        for num in nums[1:]:
            if num < prev:
                prev = num
                quo = 0
            else:
                quo, rem = divmod(num, prev)
                if rem == 0:
                    count += quo-1
                else:
                    divider = quo+1
                    count += quo
                    prev = num//divider
            
        return count