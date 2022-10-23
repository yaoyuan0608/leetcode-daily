class Solution:
    def robotWithString(self, s: str) -> str:
        # use a dic to store the remaining lexicon in s, use t to store the candidate char
        # when the smallest char in dic is larger than the last one in t, pop it out from t
        dic = Counter(s)
        t = []
        res = []
        for string in s:
            t.append(string)
            dic[string] -= 1
            if dic[string] == 0:
                del dic[string]
            # if use min(dic) > t[-1] here, the lexicon exists in t will be poped out after a larger one
            while t and dic and min(dic) >= t[-1]:
                res.append(t.pop())
        res += t[::-1]
        return ''.join(res)