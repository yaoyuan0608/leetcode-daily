class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        res = []
        start = 0
        for i in range(len(word)):
            start = (start*10 + int(word[i])) % m
            if start % m == 0:
                res.append(1)
            else:
                res.append(0)
        return res