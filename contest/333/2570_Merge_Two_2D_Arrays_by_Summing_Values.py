class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        dic1 = {}
        dic2 = {}
        ids = []
        for idx, val in nums1:
            dic1[idx] = val
            ids.append(idx)
        for idx, val in nums2:
            dic2[idx] = val
            ids.append(idx)
        
        ids = sorted(list(set(ids)))
        res = []
        for id_ in ids:
            tmp = [id_, 0]
            if id_ in dic1:
                tmp[1] += dic1[id_]
            if id_ in dic2:
                tmp[1] += dic2[id_]
            res.append(tmp)
        return res