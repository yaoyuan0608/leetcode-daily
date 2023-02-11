class Solution:
    def monkeyMove(self, n: int) -> int:
        def powerLL(x, n):
            result = 1
            while n:
                if n & 1:
                    result = result * x % MOD
                n //= 2
                x = x * x % MOD
            return result
        
        MOD = 1000000007
        res = powerLL(2, n)

        return (res-2) % MOD