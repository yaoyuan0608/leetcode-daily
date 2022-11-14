class Solution:
    def helper(self,string1, string2):
        diff = 0
        for i in range(len(string1)):
            if string1[i] != string2[i]:
                diff += 1

        return diff <= 2
    
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        res = []
        for i in range(len(queries)):
            for j in range(len(dictionary)):
                if self.helper(queries[i], dictionary[j]):
                    res.append(queries[i])
                    break
        return res