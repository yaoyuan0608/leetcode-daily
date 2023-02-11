class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def isPrime(x):
            sq = int(math.sqrt(x))
            for i in range(2, sq+1):
                if x % i == 0:
                    return False
            return True
        
        numbers = [True] * 1000001
        primes = []
        for i in range(2, right+1):
            if numbers[i]:
                if i >= left:
                    primes.append(i)
                for j in range(i**2, right+1, i):
                    numbers[j] = False
                    
        
        minimum = float('inf')
        res = [-1, -1]
        for i in range(len(primes)-1):
            a,b = primes[i], primes[i+1]
            if b-a < minimum:
                minimum = b-a
                res = [a, b]
        return res