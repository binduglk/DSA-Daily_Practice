# PROBLEM 44: Longest Substring Without Repeating Characters
# LeetCode 3
# Approach: Variable sliding window + HashSet
# Expand right freely; shrink left when duplicate enters window
# Time: O(n) | Space: O(min(n, charset))

class Solution44:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len


# --- TEST ---
sol44 = Solution44()
print(sol44.lengthOfLongestSubstring("abcabcbb"))  # Expected: 3
print(sol44.lengthOfLongestSubstring("bbbbb"))     # Expected: 1
print(sol44.lengthOfLongestSubstring("pwwkew"))    # Expected: 3
