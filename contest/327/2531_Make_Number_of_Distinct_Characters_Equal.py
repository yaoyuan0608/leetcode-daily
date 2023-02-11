class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        def helper(map1, map2):
            count1 = 0
            count2 = 0
            for i in map1:
                if i > 0:
                    count1 +=1
            for j in map2:
                if j > 0:
                    count2 += 1
            return count1 - count2
        
        map1 = [0] * 26
        map2 = [0] * 26
        count1 = 0
        count2 = 0
        
        for w1 in word1:
            alp = ord(w1) - ord('a')
            if map1[alp] == 0:
                count1 += 1
            map1[alp] += 1
            
        for w2 in word2:
            alp = ord(w2) - ord('a')
            if map2[alp] == 0:
                count2 += 1
            map2[alp] += 1
        
        diff = count1 - count2
        for i in range(26):
            for j in range(26):
                # exchange the character word2's i and word1's j
                if map2[i] != 0 and map1[j] != 0:
                    map1[i] += 1
                    map2[i] -= 1
                    map1[j] -= 1
                    map2[j] += 1
                    # determination
                    if helper(map1, map2) == 0:
                        return True
                    map1[i] -= 1
                    map2[i] += 1
                    map1[j] += 1
                    map2[j] -= 1
        return False