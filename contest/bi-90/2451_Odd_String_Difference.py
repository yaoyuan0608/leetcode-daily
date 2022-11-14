class Solution:
    def oddString(self, words: List[str]) -> str:
        def diff(string):
            res = []
            for i in range(len(string)-1):
                res.append(ord(string[i+1]) - ord(string[i]))
            return res
        
        seen = defaultdict(list)
        for word in words:
            d = diff(word)
            #d = '*'.join([str(x) for x in d])
            seen[tuple(d)].append(word)
        #print(seen)
        for key, value in seen.items():
            if len(value) == 1:
                return value[0]