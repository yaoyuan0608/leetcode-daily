class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        words_valid = []
        for word in words:
            if word[0] in ['a','e','i','o','u'] and word[-1] in ['a','e','i','o','u']:
                words_valid.append(1)
            else:
                words_valid.append(0)
        
        prefix = {0:0}
        start_sum = 0
        for i, valid in enumerate(words_valid):
            start_sum += valid
            prefix[i+1] = start_sum
        
        res = []
        for q in queries:
            s, e = q
            res.append(prefix[e+1]-prefix[s])
        return res