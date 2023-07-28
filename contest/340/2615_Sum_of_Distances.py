class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        def find(lists):
            prefix = [lists[0]]
            for i in range(1,len(lists)):
                prefix.append(prefix[-1] + lists[i])
            prefix = [0] + prefix
            prefix = prefix[:-1]
            suffix = [lists[-1]]
            for i in range(len(lists)-2, -1, -1):
                suffix.append(suffix[-1] + lists[i])
            suffix = [0] + suffix
            suffix = suffix[:-1]
            suffix = suffix[::-1]
            res = []
            #print(prefix,suffix)
            for i in range(len(lists)):
                res.append(lists[i]*(2*i+1-len(lists))-prefix[i]+suffix[i])
            return res
            
        mapping = defaultdict(list)
        for idx, num in enumerate(nums):
            mapping[num].append(idx)
        
        res = [0] * len(nums)
        for key, value in mapping.items():
            dist = find(value)
            for v,d in zip(value,dist):
                res[v] = d
        return res