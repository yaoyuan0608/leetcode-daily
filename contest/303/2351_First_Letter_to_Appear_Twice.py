class Solution:
    def repeatedCharacter(self, s: str) -> str:
        count = defaultdict(int)
        for char in s:
            if char not in count:
                count[char] = 1
            else:
                return char