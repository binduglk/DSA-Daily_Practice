# Session 1 - Unique Paths
# LeetCode #62
# Topic - 2D DP
# Day 18

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # create dp grid
        dp = [[1]*n for _ in range(m)]

        # fill dp grid
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]

# Testing
sol = Solution()
print(sol.uniquePaths(3, 7))   # 28
print(sol.uniquePaths(3, 2))   # 3
print(sol.uniquePaths(1, 1))   # 1

'''🎬 Trace:
m=3, n=3

Initial dp:
[1, 1, 1]
[1, 0, 0]
[1, 0, 0]

Fill:
i=1,j=1: dp[1][1] = dp[0][1]+dp[1][0] = 1+1 = 2
i=1,j=2: dp[1][2] = dp[0][2]+dp[1][1] = 1+2 = 3
i=2,j=1: dp[2][1] = dp[1][1]+dp[2][0] = 2+1 = 3
i=2,j=2: dp[2][2] = dp[1][2]+dp[2][1] = 3+3 = 6

Final dp:
[1, 1, 1]
[1, 2, 3]
[1, 3, 6]

return dp[2][2] = 6'''