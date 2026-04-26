# P46: Minimum Window Substring
# LeetCode 76
# Pattern: Variable Window + two frequency hashmaps
# Time: O(n + m) | Space: O(n + m)

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        need = Counter(t)       # chars we need and how many
        have = {}               # chars we have in current window
        formed = 0              # how many unique chars satisfy required count
        required = len(need)    # how many unique chars must be satisfied

        left = 0
        min_len = float("inf")
        result = ""

        for right in range(len(s)):
            char = s[right]
            have[char] = have.get(char, 0) + 1

            # Check if this char's count just met the requirement
            if char in need and have[char] == need[char]:
                formed += 1

            # Try to shrink window while all chars are satisfied
            while formed == required:
                # Update result if this window is smaller
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    result = s[left:right + 1]

                # Shrink from left
                left_char = s[left]
                have[left_char] -= 1
                if left_char in need and have[left_char] < need[left_char]:
                    formed -= 1
                left += 1

        return result


# ============================
# 🔍 Testing
# ============================

sol = Solution()

print("Test 1:", sol.minWindow("ADOBECODEBANC", "ABC"))
# Expected: "BANC"

print("Test 2:", sol.minWindow("a", "a"))
# Expected: "a"

print("Test 3:", sol.minWindow("a", "aa"))
# Expected: "" (not possible)

print("Test 4:", sol.minWindow("ab", "b"))
# Expected: "b"

print("Test 5:", sol.minWindow("aa", "aa"))
# Expected: "aa"

print("Test 6:", sol.minWindow("thisisateststring", "tist"))
# Expected: "tstri" (shortest substring containing t,i,s,t)
