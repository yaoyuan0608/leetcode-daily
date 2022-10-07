class Solution:
    def dfs(self, node, parent):
        for child in self.graph[node]:
            if child != parent:
                child_xor, child_node = self.dfs(child, node)
                self.xor[node] ^= child_xor
                self.child[node] |= child_node
        return self.xor[node], self.child[node]
                
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        # remove one edge results in two subtree, calculate the value A and B
        # for subtree a, remove another edge then the result become B, C and A^C
        # iterate on this two edge, time complexity(n^2)
        self.nums = nums
        self.xor = nums[:]
        self.child = {x: {x} for x in range(len(nums))}
        self.graph = defaultdict(set)
        for s, e in edges:
            self.graph[s].add(e)
            self.graph[e].add(s)
        
        self.total = 0
        for num in nums:
            self.total ^= num

        self.dfs(0, None)

    
        self.res = float('inf')
        for i in range(len(edges)):
            s1, e1 = edges[i]
            if e1 in self.child[s1]:
                s1, e1 = e1, s1
            for j in range(i):
                s2, e2 = edges[j]
                if e2 in self.child[s2]:
                    s2, e2 = e2, s2
                if s2 in self.child[s1] and s1 != s2:
                    cands = [self.xor[s2], self.xor[s1] ^ self.xor[s2], self.total ^ self.xor[s1]]
                elif s1 in self.child[s2] and s1 != s2:
                    cands = [self.xor[s1], self.xor[s2] ^ self.xor[s1], self.total ^ self.xor[s2]]
                else:
                    cands = [self.xor[s1], self.xor[s2], self.total ^ self.xor[s1] ^ self.xor[s2]]
                self.res = min(self.res, max(cands) - min(cands))
        return self.res