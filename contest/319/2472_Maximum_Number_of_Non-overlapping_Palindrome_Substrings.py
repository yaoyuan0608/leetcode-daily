class Solution:
    def find_pali(self, s):
        dp = [[False] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
        
        for j in range(len(s)):
            for i in range(j):
                if i+1 == j:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]
        return dp
    
    def maxPalindromes(self, s: str, k: int) -> int:
        # dp_m[i][j] represent whether s[i:j+1] is palidrome
        # start from index 0, greedy search to end, use last to store the end index of last palidrome
        dp_m = self.find_pali(s)
        res = 0
        last = -1
        for i in range(len(s)):
            for j in range(last+1,i+1):
                if dp_m[j][i] and i-j+1>=k:
                    res += 1
                    last = i
        return res