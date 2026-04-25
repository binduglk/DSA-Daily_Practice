# P44: Longest Substring Without Repeating Characters
# LeetCode 3
# Pattern: Variable window + hashmap (char → last seen index)
# Time: O(n) | Space: O(min(n, alphabet))

def length_of_longest_substring(s: str) -> int:
    char_index = {}   # char → most recent index
    left = 0          # window start
    max_len = 0

    for right in range(len(s)):
        char = s[right]

        # If char seen AND it's inside current window → shrink left
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1

        # Update last seen index
        char_index[char] = right

        # Update max length
        max_len = max(max_len, right - left + 1)

    return max_len


# ============================
# 🔍 Testing
# ============================

print("Test 1:", length_of_longest_substring("abcabcbb"))
# Expected: 3 → "abc"

print("Test 2:", length_of_longest_substring("bbbbb"))
# Expected: 1 → "b"

print("Test 3:", length_of_longest_substring("pwwkew"))
# Expected: 3 → "wke"

print("Test 4:", length_of_longest_substring(""))
# Expected: 0 → empty string

print("Test 5:", length_of_longest_substring("abba"))
# Expected: 2 → "ab" or "ba"
