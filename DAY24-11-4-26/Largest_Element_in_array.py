# DAY 21 - Striver A2Z Sheet
# Step 1: Arrays Easy
# Problem 1: Largest Element in Array

class Solution:
    def largestElement(self, arr: list[int]) -> int:
        max_val = arr[0]              # assume first element is largest

        for i in range(1, len(arr)):  # start from index 1
            if arr[i] > max_val:
                max_val = arr[i]      # update if current is bigger

        return max_val

# -------------------- VS CODE TEST --------------------
sol = Solution()
print(sol.largestElement([3, 2, 1, 5, 6, 4]))   # Expected: 6
print(sol.largestElement([1]))                    # Expected: 1
print(sol.largestElement([10, 2, 30, 4]))         # Expected: 30

'''Trace [3, 2, 1, 5, 6, 4]:

max=3 → 2<3 → 1<3 → 5>3, max=5 → 6>5, max=6 → 4<6
Return 6 ✅

Time: O(n) | Space: O(1)'''
