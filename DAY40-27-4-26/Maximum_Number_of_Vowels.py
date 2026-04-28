# P50: Maximum Number of Vowels in a Substring of Given Length
# LeetCode 1456
# Pattern: Fixed Window
# Time: O(n) | Space: O(1)

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")

        # Build first window
        window_vowels = sum(1 for c in s[:k] if c in vowels)
        max_vowels = window_vowels

        for i in range(k, len(s)):
            # Add right char
            if s[i] in vowels:
                window_vowels += 1
            # Drop left char
            if s[i - k] in vowels:
                window_vowels -= 1
            max_vowels = max(max_vowels, window_vowels)

        return max_vowels


# ============================
# 🔍 Testing
# ============================

sol = Solution()

print("Test 1:", sol.maxVowels("abciiidef", 3))
# Expected: 3 → substring "iii"

print("Test 2:", sol.maxVowels("aeiou", 2))
# Expected: 2 → any consecutive pair of vowels

print("Test 3:", sol.maxVowels("leetcode", 3))
# Expected: 2 → substring "lee"

print("Test 4:", sol.maxVowels("rhythms", 4))
# Expected: 0 → no vowels at all

print("Test 5:", sol.maxVowels("tryhard", 4))
# Expected: 1 → substring "hard" has 'a'
