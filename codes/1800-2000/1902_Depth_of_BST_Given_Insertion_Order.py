class Solution:
    def maxDepthBST(self, order: List[int]) -> int:
        # use the idea of sorted Tree
        from sortedcontainers import SortedDict
        tree = SortedDict()
        tree[0] = 0
        tree[100001] = 0
        d = {0: 0, 100001: 0}
        
        for i in order:
            j = tree.bisect_left(i)
            d[i] = 1 + max(d[tree[j - 1]], d[tree[j]])
            sl.add(i)
        return max(d.values())