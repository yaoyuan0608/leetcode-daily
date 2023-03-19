class Solution:
    def minOperations(self, n: int) -> int:
        count = 0
        while n:
            fl = math.floor(math.log2(n))
            diff_floor = n - 2**fl
            diff_ceil = 2**(fl+1) - n
            if diff_floor < diff_ceil:
                n = diff_floor
            else:
                n = diff_ceil
            count += 1
        return count