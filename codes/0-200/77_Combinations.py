class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def helper(idx, path):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(idx, n+1):
                path.append(i)
                helper(i+1, path)
                path.pop()

        res = []
        helper(1, [])
        return res