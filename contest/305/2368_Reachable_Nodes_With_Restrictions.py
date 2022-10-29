class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        if not edges:
            return 0
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        seen = set()
        for i in restricted:
            seen.add(i)
        q = deque([])
        q.append(0)
        count = 0
        while q:
            node = q.popleft()
            seen.add(node)
            count += 1
            for child in graph[node]:
                if child not in seen:
                    q.append(child)
        return count