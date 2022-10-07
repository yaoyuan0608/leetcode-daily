class Solution:
    def helper(self, node):
        if not self.graph[node]:
            self.res = max(self.res, 1)
            return 1
        
        max1, max2 = 0, 0
        for child in self.graph[node]:
            child_path = self.helper(child)
            if self.s[child] == self.s[node]:
                child_path = 0
            if child_path > max1:
                max1, max2 = child_path, max1
            elif child_path > max2:
                max2 = child_path
        self.res = max(self.res, max1 + max2 + 1)
        return max1 + 1
    
    def longestPath(self, parent: List[int], s: str) -> int:
        # recursive, similar to find the longest path with same value
        # store the length of each child and find the maximum
        self.res = 0
        self.parent = parent
        self.s = s
        self.graph = defaultdict(list)
        for idx, val in enumerate(parent):
            if val != -1:
                self.graph[val].append(idx)

        self.helper(0)
        return self.res