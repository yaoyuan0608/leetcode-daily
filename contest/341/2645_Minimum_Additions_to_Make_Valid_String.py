class Solution:
    def addMinimum(self, word: str) -> int:
        # find a way to split word
        word += '.'
        split = []
        last = ''
        tmp = ''
        for w in word:
            if w > last:
                last = w
                tmp += w
            else:
                split.append(tmp)
                last = w
                tmp = w
        #split.append(tmp)
        #print(split)
        return sum([3-len(x) for x in split])