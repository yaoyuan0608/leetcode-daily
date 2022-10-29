class Solution:
    def dfs(self, node, count, count_list):
        if node in self.visited:
            # need to check whether the current node has been visited in this loop before
            if node in count_list:
                self.length = max(self.length, count-count_list[node])
            return False
        
        self.visited.add(node)
        count_list[node] = count
        if self.edges[node] != -1:
            if not self.dfs(self.edges[node], count+1, count_list):
                return False
        self.visited.remove(node)
        return True
    
    def longestCycle(self, edges: List[int]) -> int:
        # self.visited is used to skip unnecessary starting point
        self.edges = edges
        self.visited = set()
        self.length = -1
        for i in range(len(edges)):
            if i not in self.visited:
                self.dfs(i, 0, defaultdict(int))
        return self.length
