# Session 3 - Word Break
# LeetCode #139
# Topic - DP + String
# Day 18

class Solution:
    def wordBreak(self, s: str,
                  wordDict: list) -> bool:
        word_set = set(wordDict)   # O(1) lookup!
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True               # empty string!

        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]

# Testing
sol = Solution()
print(sol.wordBreak("leetcode",
      ["leet","code"]))              # True
print(sol.wordBreak("applepenapple",
      ["apple","pen"]))              # True
print(sol.wordBreak("catsandog",
      ["cats","dog","sand","an","cat"]))  # False