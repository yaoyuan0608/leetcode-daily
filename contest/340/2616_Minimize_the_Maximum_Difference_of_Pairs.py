class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        def find(x):
            count = 0
            i = 0
            j = 1
            while i < (len(nums) - 1):
                while j < len(nums) and nums[j] - nums[i] <= x:
                    j += 1
                count += (j - i) // 2
                #print(j,i,count,x)
                if (j-i)%2 == 0 or j-i==1:
                    i = j
                    j = i+1
                else:
                    i = j-1
                if count >= p:
                    return True
            return False
        
        if len(nums) <= 1:
            return 0
        nums = sorted(nums)
        left = 0
        right = nums[-1] - nums[0] + 1
        while left < right:
            mid = left + (right - left) // 2
            if find(mid):
                right = mid
            else:
                left = mid + 1
        return left