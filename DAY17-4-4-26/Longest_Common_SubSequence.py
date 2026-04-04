# Session 3 - Longest Common Subsequence
# LeetCode #1143
# Topic - 2D Dynamic Programming
# Day 14

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        # create 2D dp array
        dp = [[0] * (n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[m][n]

# Testing
sol = Solution()
print(sol.longestCommonSubsequence("abcde", "ace"))   # 3
print(sol.longestCommonSubsequence("abc", "abc"))      # 3
print(sol.longestCommonSubsequence("abc", "def"))      # 0