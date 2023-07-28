class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        res = []
        seen = set()
        seen.add(1)
        start = 1
        count = 1
        while True:
            nex = (start + count * k)%n
            if nex == 0:
                nex = n
            if nex in seen:
                break
            seen.add(nex)
            count += 1
            start = nex
        
        for i in range(1, n+1):
            if i not in seen:
                res.append(i)
        return res