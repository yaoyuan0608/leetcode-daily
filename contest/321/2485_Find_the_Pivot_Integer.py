class Solution:
    def pivotInteger(self, n: int) -> int:
        res = math.sqrt((n*n+n)//2)
        if int(res) == res:
            return int(res)
        else:
            return -1