class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # graph problem, decide whether we can reach a given node
        def dfs(x):
            if arr[x] == 0:
                return True
            if x in seen:
                return False
            seen.add(x)
            candidates = [x + arr[x], x - arr[x]]
            for can in candidates:
                if 0 <= can < len(arr):
                    if dfs(can):
                        return True
            return False
        seen = set()
        return dfs(start)