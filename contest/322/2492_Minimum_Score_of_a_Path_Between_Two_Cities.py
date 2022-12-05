class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b, d in roads:
            graph[a].append((b,d))
            graph[b].append((a,d))
        
        res = float('inf')
        seen = set()
        q = deque([])
        q.append(1)
        seen.add((-1,1))
        # traverse each edge and find the minimum
        while q:
            node = q.popleft()
            for child, dist in graph[node]:
                if (node,child) not in seen:
                    res = min(res, dist)
                    q.append(child)
                    seen.add((node,child))
                    seen.add((child,node))
        return res