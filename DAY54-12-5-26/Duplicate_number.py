# Problem : Contains Duplicate

class Solution:
    def containsDuplicate(self, nums):
        s = set()
        for n in nums:
            if n in s:
                return True
        s.add(n)
        return False
    
# Time Complexity: O(n)
# Space Complexity: O(n)