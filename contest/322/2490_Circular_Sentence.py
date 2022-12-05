class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sen = sentence.split(' ')
        first = sen[0][0]
        for i in range(1, len(sen)):
            # current start is last end
            if sen[i-1][-1] != sen[i][0]:
                return False
        if sen[-1][-1] != first:
            return False
        else:
            return True