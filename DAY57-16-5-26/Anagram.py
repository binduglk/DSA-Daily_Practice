from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):

        ans = defaultdict(list)

        for word in strs:

            key = "".join(sorted(word))

            ans[key].append(word)

        return list(ans.values())


sol = Solution()
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))