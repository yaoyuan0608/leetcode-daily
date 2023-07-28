class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        def find_path(node, end, degree, seen):
            if node == end:
                return degree, True
            for child in graph[node]:
                if child not in seen:
                    seen.add(child)
                    degree[child] += 1
                    degree, found = find_path(child, end, degree, seen)
                    if found:
                        return degree, True
                    degree[child] -= 1
                    seen.remove(child)
            return degree, False
        
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        degree = [0] * n
        for s, e in trips:
            degree[s] += 1
            seen = {s}
            degree,_ = find_path(s, e, degree, seen)
        
        def dfs(node, parent):
            not_halve = price[node] * degree[node]
            halve = not_halve // 2
            for child in graph[node]:
                if child != parent:
                    nh, h = dfs(child, node)
                    not_halve += min(nh, h)  # node not change, child can change or stay
                    halve += nh  # node change, child can only stay
            return not_halve, halve
        return min(dfs(0, -1))