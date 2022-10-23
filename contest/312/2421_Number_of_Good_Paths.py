class Solution:
    # union find
    def find(self, x):
        while x != self.graph[x]:
            self.graph[x] = self.graph[self.graph[x]]
            x = self.graph[x]
        return x
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.graph[px] = self.graph[py]
            
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        self.value = defaultdict(list)
        self.graph = [i for i in range(len(vals))]
        self.value_edge = defaultdict(list)
        
        for a, b in edges:
            self.value_edge[max(vals[a], vals[b])].append((a,b))
        for idx, val in enumerate(vals):
            self.value[val].append(idx)
        
        res = 0
        # starting from the edge with the least value, which means their neighbors are all smaller
        for val in sorted(self.value.keys()):
            for i, j in self.value_edge[val]:
                # union the edge with larger value
                self.union(i, j)
            count = defaultdict(int)
            for node in self.value[val]:
                count[self.find(node)] += 1
            # group all node with the same parent
            for group in count:
                res += (count[group] * (count[group] + 1))//2

        return res