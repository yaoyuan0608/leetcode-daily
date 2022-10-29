class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        if node1 == node2:
            return node1
        
        dist = 0
        visited1 = set()
        visited2 = set()
        q = deque([])
        q.append((node1,-1))
        q.append((node2,1))
        visited1.add(node1)
        visited2.add(node2)
        res = []
        while q:
            dist += 1
            for _ in range(len(q)):
                node,source = q.popleft()
                if edges[node] != -1:
                    child = edges[node]
                    if source == -1:
                        if child in visited1:
                            continue
                        elif child in visited2:
                            res.append((dist,child))
                        else:
                            q.append((child,-1))
                            visited1.add(child)
                    else:
                        if child in visited2:
                            continue
                        elif child in visited1:
                            res.append((dist,child))
                        else:
                            q.append((child,1))
                            visited2.add(child)
        if not res:
            return -1
        res = sorted(res,key=lambda x: (x[0],x[1]))
        return res[0][1]