class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        d = defaultdict(int)
        for k1, v1 in items1:
            d[k1] += v1
        for k2, v2 in items2:
            d[k2] += v2

        res = []
        for key in d:
            res.append([key, d[key]])
        return sorted(res, key=lambda x:x[0])