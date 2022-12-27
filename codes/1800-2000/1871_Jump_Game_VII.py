class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        # graph problem, use bfs to decide whether we can reach a node
        # longest is a helper variable that stores the longest index passed by in last step
        q = collections.deque([])
        q.append(0)
        longest = 0
        while q:
            idx = q.popleft()
            # we can skip those index before longest, to prevent repeated computation
            for j in range(max(idx + minJump, longest+1), min(idx + maxJump, len(s) - 1) + 1):
                if s[j] == '0':
                    if j == len(s) - 1:
                        return True
                    q.append(j)
            longest = idx + maxJump
        return False