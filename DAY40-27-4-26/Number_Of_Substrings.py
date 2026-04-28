# P49: Number of Substrings Containing All Three Characters
# LeetCode 1358
# Problem: Given a string s consisting only of characters 'a', 'b', and 'c',
# return the number of substrings containing at least one occurrence of all three characters.
# ============================================================
# Pattern: Variable Window — shrink when all 3 chars present
# Key insight: once window has a,b,c → every extension to the right is also valid
# Time: O(n) | Space: O(1)

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = {"a": 0, "b": 0, "c": 0}
        left = 0
        result = 0

        for right in range(len(s)):
            count[s[right]] += 1

            # All 3 chars present → shrink and count
            while count["a"] > 0 and count["b"] > 0 and count["c"] > 0:
                # Every extension from right to end is also valid
                result += len(s) - right
                count[s[left]] -= 1
                left += 1

        return result


# ============================
# 🔍 Testing
# ============================

sol = Solution()

print("Test 1:", sol.numberOfSubstrings("abcabc"))
# Expected: 10 → multiple substrings containing a,b,c

print("Test 2:", sol.numberOfSubstrings("aaacb"))
# Expected: 3 → substrings: "aaacb", "aacb", "acb"

print("Test 3:", sol.numberOfSubstrings("abc"))
# Expected: 1 → only "abc"

print("Test 4:", sol.numberOfSubstrings("aaaa"))
# Expected: 0 → no substring contains all three chars

print("Test 5:", sol.numberOfSubstrings("abccba"))
# Expected: 9 → several substrings containing all three
