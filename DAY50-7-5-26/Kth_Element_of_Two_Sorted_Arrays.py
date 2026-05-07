'''PROBLEM : Kth Element of Two Sorted Arrays
Concept Problem (Binary Search Partition Method)
Problem: Given two sorted arrays arr1 and arr2, find the kth element in the merged sorted array.
Approach: Binary search on partition size. Ensure left partition ≤ right partition.
Time: O(log(min(n,m))) | Space: O(1)'''

def kthElement(arr1, arr2, k):
    n, m = len(arr1), len(arr2)
    if n > m:
        return kthElement(arr2, arr1, k)

    low, high = max(0, k - m), min(k, n)

    while low <= high:
        cut1 = (low + high) // 2
        cut2 = k - cut1

        left1 = arr1[cut1 - 1] if cut1 > 0 else float('-inf')
        left2 = arr2[cut2 - 1] if cut2 > 0 else float('-inf')
        right1 = arr1[cut1] if cut1 < n else float('inf')
        right2 = arr2[cut2] if cut2 < m else float('inf')

        if left1 <= right2 and left2 <= right1:
            return max(left1, left2)
        elif left1 > right2:
            high = cut1 - 1
        else:
            low = cut1 + 1


# --- TEST ---
print(kthElement([2,3,6,7,9], [1,4,8,10], 5))  # Expected: 6
print(kthElement([100,112,256,349,770], [72,86,113,119,265,445,892], 7)) # Expected: 256
