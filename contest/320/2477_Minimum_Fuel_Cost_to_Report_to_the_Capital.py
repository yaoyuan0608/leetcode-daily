class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        #start from 0, dfs to all other node, store the number of node passed.
        self.tree = defaultdict(list)
        for a,b in roads:
            self.tree[a].append(b)
            self.tree[b].append(a)
        
        def dfs(node, parent):
            cost, people = 0, 1
            for child in self.tree[node]:
                if child != parent:
                    cost_, people_ = dfs(child, node)
                    cost += cost_
                    people += people_
            # ceil(people/seats) represents the total number of car you need to drive all these people
            return cost+ceil(people/seats), people
        res = 0
        for i in (self.tree[0]):
            res += dfs(i, 0)[0]
        return res