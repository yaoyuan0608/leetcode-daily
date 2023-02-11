class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        arr = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            for j in range(i):
                arr[i][nums[j]] += 1
        
            for j in range(1, n + 1):
                arr[i][j] += arr[i][j - 1]
        
        for i in range(n):
            for j in range(i + 1, n):
                if nums[j] < nums[i]:
                    ans += arr[i][nums[j]] * (n + arr[j][nums[i]] - arr[-1][nums[i]] - arr[j][-1])
                    
        return ans