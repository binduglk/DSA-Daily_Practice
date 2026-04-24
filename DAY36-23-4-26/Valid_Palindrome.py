# PROBLEM 37: Valid Palindrome
# LeetCode 125
# Question: A phrase is a palindrome if, after converting all uppercase letters 
# into lowercase letters and removing all non-alphanumeric characters, 
# it reads the same forward and backward. 
# Given a string s, return true if it is a palindrome, or false otherwise.
# ============================================================

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            # skip non-alphanumeric characters
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            # compare lowercase characters
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True


# ============================
# 🔍 Testing
# ============================

sol = Solution()

print("Test 1:", sol.isPalindrome("A man, a plan, a canal: Panama"))
# Expected: True → "amanaplanacanalpanama" is a palindrome

print("Test 2:", sol.isPalindrome("race a car"))
# Expected: False → "raceacar" is not a palindrome

print("Test 3:", sol.isPalindrome(" "))
# Expected: True → empty string after removing non-alphanumeric

print("Test 4:", sol.isPalindrome("No lemon, no melon"))
# Expected: True → "nolemonnomelon" is a palindrome

print("Test 5:", sol.isPalindrome("Was it a car or a cat I saw?"))
# Expected: True → classic palindrome phrase
