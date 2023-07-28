class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(x,y):
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py
                return True
            else:
                return False
        parent = [i for i in range(n)]
        graph = defaultdict(list)
        for a,b in edges:
            union(a,b)
            graph[a].append(b)
            graph[b].append(a)
        
        count = 0
        group = defaultdict(list)
        for i in range(n):
            pi = find(i)
            group[pi].append(i)
        
        for key, value in group.items():
            total_edge = 0
            for val in value:
                total_edge += len(graph[val])
            if total_edge == len(value) * (len(value)-1):
                count += 1
        return count