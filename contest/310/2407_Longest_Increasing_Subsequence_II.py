class segment:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * 2 * self.n
    def query(self, l, r):
        l += self.n
        r += self.n
        res = 0
        while l < r:
            # odd value
            if l&1:
                res = max(res, self.tree[l])
                l += 1
            if r&1:
                r -= 1
                res = max(res, self.tree[r])
            l //= 2
            r //= 2
        return res
    def update(self, idx, val):
        idx += self.n
        self.tree[idx] = val
        while idx > 1:
            idx //= 2
            self.tree[idx] = max(self.tree[idx*2], self.tree[idx*2+1])
            
class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        # k perform as the window size on a segment tree
        n = max(nums)
        res = 1
        seg = segment(n)
        for num in nums:
            # 1-index to 0-index
            num -= 1
            # find the maximum value from tree[num-k:num]
            premax = seg.query(max(0, num-k), num) + 1
            res = max(res, premax)
            seg.update(num, premax)
        return res
            