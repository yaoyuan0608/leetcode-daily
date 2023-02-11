class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        degree = [0] * n
        
        for a, b in edges:
            a -= 1
            b -= 1
            graph[a].append(b)
            graph[b].append(a)
            degree[b] += 1
            degree[a] += 1
        # one more edge can help to increase two odd nodes
        # if the node has maximum number of edge, it cannot be connected
        #print(graph, degree)
        odds = []
        for i in range(len(degree)):
            if degree[i] == n-1:
                if degree[i] % 2 == 1:
                    return False
            else:
                if degree[i] % 2 == 1:
                    odds.append(i)
                else:
                    continue
        #print(odds)
        if len(odds) > 4:
            return False
        elif len(odds) == 0:
            return True
        
        # for those odd nodes, if they are connected with each other, then return false
        elif len(odds) == 2:
            node1 = odds[0]
            node2 = odds[1]
            edge1 = graph[node1]
            edge2 = graph[node2]
            for k in range(n):
                if k not in set(edge1) and k not in set(edge2):
                    return True
            return False
        elif len(odds) == 4:
            node1, node2, node3, node4 = odds[0], odds[1], odds[2], odds[3]
            flag = (node1 not in graph[node2] and node3 not in graph[node4]) or (node1 not in graph[node3] and node2 not in graph[node4]) or (node1 not in graph[node4] and node3 not in graph[node2])
            return flag
