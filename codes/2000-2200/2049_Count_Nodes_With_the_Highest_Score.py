class Solution:
    def helper(self, node):
        
        if node not in self.graph:
            count = self.total-1
            if count > self.maximum:
                self.maximum = count
                self.res = 1
            elif count == self.maximum:
                self.res += 1
            return 1
        
        if len(self.graph[node]) == 2:
            left = self.helper(self.graph[node][0])
            right = self.helper(self.graph[node][1])
            if node == 0:
                count = left*right
            else:
                count = left*right*(self.total-left-right-1)
            if count > self.maximum:
                self.maximum = count
                self.res = 1
            elif count == self.maximum:
                self.res += 1
            return left + right + 1
        
        elif len(self.graph[node]) == 1:
            child = self.helper(self.graph[node][0])
            if node == 0:
                count = self.total - 1
            else:
                count = child*(self.total-child-1)
            if count > self.maximum:
                self.maximum = count
                self.res = 1
            elif count == self.maximum:
                self.res += 1
            return child + 1
        
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        # recursive, use left and right to store the number of nodes of subtree
        self.total = len(parents)
        self.maximum = 0
        self.res = 0
        self.graph = defaultdict(list)
        for idx, val in enumerate(parents):
            if val != -1:
                self.graph[val].append(idx)

        self.helper(0)
        return self.res