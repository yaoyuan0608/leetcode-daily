class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        def find_id(c):
            maximum = float('-inf')
            res = ''
            id_list = creator_id[c]
            for i, idx in id_list:
                if views[idx] > maximum:
                    maximum = views[idx]
                    res = i
                elif views[idx] == maximum:
                    if i < res:
                        res = i
            return res
        
        creator_view = defaultdict(int)
        creator_id = defaultdict(list)
        
        for idx in range(len(creators)):
            c, v, i = creators[idx], views[idx], ids[idx]
            creator_view[c] += v
            creator_id[c].append((i, idx))

        res = []
        maximum_view = max(creator_view.values())
        for key, val in creator_view.items():
            tmp = []
            if val == maximum_view:
                tmp.append(key)
                tmp.append(find_id(key))
            if tmp:
                res.append(tmp)
        return res
