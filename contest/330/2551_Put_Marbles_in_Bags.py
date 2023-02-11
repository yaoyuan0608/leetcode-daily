class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        seen = []
        for i in range(1, len(weights)):
            seen.append(weights[i]+weights[i-1])
        seen = sorted(seen)
        print(seen)
        if k == 1:
            return 0
        else:
            biggest = sum(seen[-(k-1):])
            smallest = sum(seen[:(k-1)])
            print(biggest, smallest)
            return biggest - smallest