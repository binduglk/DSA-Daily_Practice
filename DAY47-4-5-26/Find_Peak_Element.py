'''PROBLEM : Find Peak Element
LeetCode 162
Problem: A peak element is one that is greater than its neighbors. Return the index of any peak.
Approach: Binary search — if nums[mid] < nums[mid+1], peak lies to the right; else to the left.
Time: O(log n) | Space: O(1)'''

def findPeakElement(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left


# --- TEST ---
print(findPeakElement([1,2,3,1]))       # Expected: 2 (nums[2]=3)
print(findPeakElement([1,2,1,3,5,6,4])) # Expected: 5 (nums[5]=6)
