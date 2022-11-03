class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        # sliding window problem, find the windows which contains 5 vowels
        # = contains at most 5 vowels - contains at most 4 vowels
        from collections import defaultdict
        def helper(maximum):
            left, right = 0, 0
            res = 0
            count = defaultdict(int)
            for right in range(len(word)):
                if word[right] in ['a', 'e', 'i', 'o', 'u']:
                    count[word[right]] += 1
                    while len(count) > maximum and left <= right:
                        tmp = word[left]
                        count[tmp] -= 1
                        left += 1
                        if count[tmp] == 0:
                            del count[tmp]
                    if left <= right:
                        res += right - left + 1
                else:
                    count = defaultdict(int)
                    left = right + 1
            return res
        return helper(5) - helper(4)