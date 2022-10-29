class Solution:
    def check(self, arr):
        if len(arr) == 2 and len(set(arr)) == 1:
            return True
        elif len(arr) == 3 and len(set(arr)) == 1:
            return True
        elif len(arr) == 3 and arr[0]-arr[1] == -1 and arr[1]-arr[2] == -1:
            return True
        else:
            return False
        
    def backtrack(self, idx):
        if idx in self.memo:
            return self.memo[idx]
        if idx == self.n:
            return True
        if idx == self.n-1:
            return False
        if idx == self.n-2 and self.nums[idx] == self.nums[idx+1]:
            return True
        if idx == self.n-2 and self.nums[idx] != self.nums[idx+1]:
            return False
        
        candidates = [[self.nums[idx], self.nums[idx+1]], [self.nums[idx], self.nums[idx+1], self.nums[idx+2]]]
        for can in candidates:
            if self.check(can):
                if self.backtrack(idx + len(can)):
                    return True
        self.memo[idx] = False
        return False
    def validPartition(self, nums: List[int]) -> bool:
        self.n = len(nums)
        self.nums = nums
        self.memo = dict()
        return self.backtrack(0)