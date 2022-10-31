class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        # dp[i]: the number of people who will share the secret at day i
        dp = [0] * (n+1)
        dp[1] = 1
        share = 0
        mod = 10 ** 9 + 7
        for i in range(2, n+1):
            # the idea of sliding window, that dp[i-delay] will start sharing secret and
            # dp[i-forget] will ending sharing secret
            share = (share + dp[i - delay] - dp[i - forget]) % mod
            dp[i] = share
        #dp[n-forget:], the number of people still remember the secret
        return sum(dp[n+1-forget:]) % mod