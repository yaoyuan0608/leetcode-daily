class Solution:
    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:
        # from the node 1 to root, all nodes has smallest missing value = 1
        res = [1] * len(nums)
        if 1 not in nums:
            return res
        # create a graph to track downward from node to child
        graph = defaultdict(list)
        for idx, p in enumerate(parents):
            graph[p].append(idx)
        # add existing value to seen
        def dfs(i):
            if nums[i] not in seen:
                for j in graph[i]:
                    dfs(j)
                seen.add(nums[i])
        
        seen = set()
        i = nums.index(1)
        miss = 1
        # start from 1, put all values in its subtree to seen
        # then we can find out the next smallest missing value
        while i >= 0:
            dfs(i)
            while miss in seen:
                miss += 1
            res[i] = miss
            i = parents[i]
        return res