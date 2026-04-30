'''PROBLEM : Longest Repeating Character Replacement
LeetCode 424
Problem: Given a string s and an integer k, return the length of the longest substring containing the same letter you can get after performing at most k replacements.
Approach: Variable window + frequency map.
Key Insight: Window is valid if (window_size - max_freq_char) <= k. We can replace the non-dominant chars (at most k of them).
Time: O(n) | Space: O(1) — at most 26 keys.'''

class Solution51:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        left = 0
        max_freq = 0
        max_len = 0

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1
            max_freq = max(max_freq, freq[s[right]])

            window_size = right - left + 1
            if window_size - max_freq > k:
                freq[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len


# --- TEST ---
sol51 = Solution51()
print(sol51.characterReplacement("ABAB", 2))     # Expected: 4
print(sol51.characterReplacement("AABABBA", 1))  # Expected: 4
print(sol51.characterReplacement("AAAA", 2))     # Expected: 4
print(sol51.characterReplacement("ABCDE", 1))    # Expected: 2
