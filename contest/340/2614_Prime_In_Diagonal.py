class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def sieve_of_eratosthenes(n):
            primes = [True] * (n+1)
            primes[0] = False
            primes[1] = False
            for i in range(2, int(n**0.5)+1):
                if primes[i]:
                    for j in range(i**2, n+1, i):
                        primes[j] = False
            return primes
        
        maximum = max([max(row) for row in nums])
        primes = sieve_of_eratosthenes(maximum+1)
        res = 0
        for i in range(len(nums)):
            if primes[nums[i][i]]:
                res = max(res, nums[i][i])
            if primes[nums[i][len(nums)-i-1]]:
                res = max(res, nums[i][len(nums)-i-1])
        return res