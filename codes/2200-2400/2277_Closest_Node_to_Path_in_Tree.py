class Solution:
    def dfs(self, start, end):
        def helper(node, path, seen):
            if node == end:
                return path
            for nei in self.graph[node]:
                if nei not in seen:
                    path.append(nei)
                    seen.add(node)
                    if helper(nei, path, seen):
                        return path
                    path.pop()
            return []
        return helper(start, [start], {start})
    
    def bfs(self, node, pool):
        q = deque([])
        q.append((node,0))
        seen = set()
        seen.add(node)
        while q:
            node, dist = q.popleft()
            if node in pool:
                return node
            for nei in self.graph[node]:
                if nei not in seen:
                    seen.add(nei)
                    q.append((nei, dist+1))
        return -1
    
    def closestNode(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        # create a graph first, for each query, store path nodes in a set first, then use bfs from node until find one in set.
        self.graph = defaultdict(list)
        for s, e in edges:
            self.graph[s].append(e)
            self.graph[e].append(s)
        
        self.res = []
        for query_ in query:
            start, end, node = query_
            pool = self.dfs(start, end)
            res_ = self.bfs(node, pool)
            self.res.append(res_)
        return self.res