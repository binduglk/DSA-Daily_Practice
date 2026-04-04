# Session 2 - Coin Change
# LeetCode #322
# Topic - 1D Dynamic Programming
# Day 14

class Solution:
    def coinChange(self, coins: list, amount: int) -> int:
        # dp array filled with infinity
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0    # 0 coins needed for amount 0!

        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i-coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1

# Testing
sol = Solution()
print(sol.coinChange([1,5,11], 15))   # 3
print(sol.coinChange([1,2,5], 11))    # 3
print(sol.coinChange([2], 3))         # -1