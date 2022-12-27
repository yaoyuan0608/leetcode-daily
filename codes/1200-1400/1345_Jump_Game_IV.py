class Solution:
    def minJumps(self, arr: List[int]) -> int:
        # graph problem, use bfs to find the shortest path
        idx_map = collections.defaultdict(list)
        for i, a in enumerate(arr):
            idx_map[a].append(i)
        
        q = collections.deque([])
        q.append(0)
        seen = {0}
        count = 0

        while q:
            for _ in range(len(q)):
                idx = q.popleft()
                if idx == len(arr) - 1:
                    return count
                for child in [idx+1, idx-1] + idx_map[arr[idx]]:
                    if 0 <= child < len(arr) and child != idx and child not in seen:
                        q.append(child)
                        seen.add(child)
                # need to update the hashmap, to reduce the computation complexity
                # e.g., if all values are the same, then the removal can prevent the future elements go through the same list again
                del idx_map[arr[idx]]
            count += 1
        return -1