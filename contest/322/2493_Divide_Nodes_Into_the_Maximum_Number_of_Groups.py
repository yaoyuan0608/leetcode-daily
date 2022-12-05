class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a-1].append(b-1)
            graph[b-1].append(a-1)
        
        seen = [0] * (n+1)
        group = []
        # group all nodes in one tree
        for i in range(n):
            if not seen[i]:
                seen[i] = 1
                stack = [i]
                group.append([i])
                while stack:
                    node = stack.pop()
                    for child in graph[node]:
                        if not seen[child]:
                            seen[child] = seen[node] + 1
                            stack.append(child)
                            group[-1].append(child)
                        # check whether the child is legal
                        elif seen[child] & 1 == seen[node] & 1:
                            return -1
        # find the minimum number of levels
        def bfs(i):
            res = 0
            seen = set()
            q = deque([])
            q.append(i)
            seen.add(i)
            while q:
                res += 1
                for _ in range(len(q)):
                    node = q.popleft()
                    for child in graph[node]:
                        if child not in seen:
                            seen.add(child)
                            q.append(child)
            return res

        res = 0
        for g in group:
            res += max(bfs(i) for i in g)
        return res