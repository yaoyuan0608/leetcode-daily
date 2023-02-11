class Solution:
    def smallestValue(self, n: int) -> int:
        def prime(x):
            res = []
            c = 2
            while x > 1:
                if x % c == 0:
                    res.append(c)
                    x = x // c
                else:
                    c = c + 1
            return res
        
        def helper(x):
            old = None
            while x != old:
                old = x
                alls = prime(x)
                x = sum(alls)
            return x
        return helper(n)