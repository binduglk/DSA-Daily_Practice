# Problem 2: Second Largest Element in Array

class Solution:
    def secondLargest(self, arr: list[int]) -> int:
        largest = float('-inf')
        second = float('-inf')

        for num in arr:
            if num > largest:
                second = largest      # old largest becomes second
                largest = num         # update largest
            elif num > second and num != largest:
                second = num          # update second only

        return second if second != float('-inf') else -1  # -1 if not found

# -------------------- VS CODE TEST --------------------
sol = Solution()
print(sol.secondLargest([3, 2, 1, 5, 6, 4]))   # Expected: 5
print(sol.secondLargest([10, 10, 10]))           # Expected: -1 (all same)
print(sol.secondLargest([1, 2]))                 # Expected: 1

'''Trace [3, 2, 1, 5, 6, 4]:

num=3 → largest=3, second=-inf
num=2 → second=2
num=5 → second=3, largest=5
num=6 → second=5, largest=6
Return 5 ✅

Time: O(n) | Space: O(1)'''