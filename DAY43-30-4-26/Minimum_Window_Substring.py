'''PROBLEM 49: Minimum Window Substring
LeetCode 76
Problem: Given two strings s and t, return the minimum window substring of s that contains all the characters of t. If no such substring exists, return ""
Approach: Variable window + two HashMaps. Expand right until all chars of t are covered, then shrink left to find the minimum valid window.
Time: O(n + m) | Space: O(m), where m = len(t).'''

from collections import Counter

class Solution49:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        need = Counter(t)
        have = {}
        formed = 0
        required = len(need)

        left = 0
        min_len = float('inf')
        result = ""

        for right in range(len(s)):
            ch = s[right]
            have[ch] = have.get(ch, 0) + 1

            if ch in need and have[ch] == need[ch]:
                formed += 1

            while formed == required:
                window_len = right - left + 1
                if window_len < min_len:
                    min_len = window_len
                    result = s[left:right + 1]

                left_ch = s[left]
                have[left_ch] -= 1
                if left_ch in need and have[left_ch] < need[left_ch]:
                    formed -= 1
                left += 1

        return result


# --- TEST ---
sol49 = Solution49()
print(sol49.minWindow("ADOBECODEBANC", "ABC"))  # Expected: "BANC"
print(sol49.minWindow("a", "a"))                # Expected: "a"
print(sol49.minWindow("a", "aa"))               # Expected: ""
