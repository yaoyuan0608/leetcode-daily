class Solution:
    def distinctIntegers(self, n: int) -> int:
        seen = set()
        seen.add(n)
        q = deque([])
        q.append(n)
        while q:
            node = q.popleft()
            for i in range(1, n+1):
                if node%i == 1:
                    q.append(i)
                    seen.add(i)
                
        return len(seen)