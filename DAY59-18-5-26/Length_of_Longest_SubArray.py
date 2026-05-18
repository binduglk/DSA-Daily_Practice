class Solution:

    def lengthOfLongestSubstring(self, s):

        char_set = set()

        left = 0
        maxi = 0

        for right in range(len(s)):

            # duplicate found
            while s[right] in char_set:

                char_set.remove(s[left])

                left += 1

            # add current character
            char_set.add(s[right])

            # update maximum length
            maxi = max(maxi, right - left + 1)

        return maxi


sol = Solution()

print(sol.lengthOfLongestSubstring("abcabcbb"))