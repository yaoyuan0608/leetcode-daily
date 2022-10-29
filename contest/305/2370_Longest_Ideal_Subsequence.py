class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        # dp[i] the longest string ending with s[i]
        # dp[i] = dp[i-1] + 1 if abs(s[i]-s[i-1]) <=k
        location = {}
        for i in range(len(s)):
            s_value = ord(s[i])
            local_max = 1
            for k_value in range(max(97, s_value-k), min(122,s_value+k)+1):
                char = chr(k_value)
                if char in location:
                    local_max = max(local_max, location[char]+1)
            location[s[i]] = local_max
        return max(location.values())