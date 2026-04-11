# Problem 3: Check if Array is Sorted and Rotated
# (Basic version: strictly sorted check)

class Solution:
    def isSorted(self, arr: list[int]) -> bool:
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:   # found a drop → not sorted
                return False
        return True                    # no drops found → sorted

# -------------------- VS CODE TEST --------------------
sol = Solution()
print(sol.isSorted([1, 2, 3, 4, 5]))    # Expected: True
print(sol.isSorted([1, 3, 2, 4, 5]))    # Expected: False
print(sol.isSorted([5]))                 # Expected: True
print(sol.isSorted([1, 1, 1]))           # Expected: True (equal is fine)