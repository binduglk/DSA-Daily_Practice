'''PROBLEM : Kth Missing Positive Number
LeetCode 1539
Problem: Given a sorted array of positive integers and an integer k, return the kth missing positive number.
Approach: Binary search — missing numbers before index i = arr[i] - (i+1).
Time: O(log n) | Space: O(1)'''

def findKthPositive(arr, k):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        missing = arr[mid] - (mid + 1)

        if missing < k:
            left = mid + 1
        else:
            right = mid - 1

    return left + k


# --- TEST ---
print(findKthPositive([2,3,4,7,11], 5))  # Expected: 9
print(findKthPositive([1,2,3,4], 2))     # Expected: 6
