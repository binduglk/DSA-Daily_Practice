'''PROBLEM : Median of Two Sorted Arrays
LeetCode 4
Problem: Given two sorted arrays nums1 and nums2, return the median of the two arrays.
Approach: Binary search on partition of the smaller array
Partition arr1 at cut1, arr2 at cut2 = (n1+n2+1)//2 - cut1.
Valid when left1 <= right2 AND left2 <= right1.
Median = max(left1,left2) if total odd, else (max(left1,left2) + min(right1,right2))/2.
Time: O(log(min(n1,n2))) | Space: O(1)'''

class Solution70:
    def findMedianSortedArrays(self, nums1: list[float], nums2: list[float]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        m, n = len(nums1), len(nums2)
        half = (m + n + 1) // 2
        low, high = 0, m

        while low <= high:
            cut1 = low + (high - low) // 2
            cut2 = half - cut1

            left1  = nums1[cut1 - 1] if cut1 > 0 else float('-inf')
            left2  = nums2[cut2 - 1] if cut2 > 0 else float('-inf')
            right1 = nums1[cut1]     if cut1 < m else float('inf')
            right2 = nums2[cut2]     if cut2 < n else float('inf')

            if left1 <= right2 and left2 <= right1:
                if (m + n) % 2 == 1:
                    return float(max(left1, left2))
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2.0
            elif left1 > right2:
                high = cut1 - 1
            else:
                low = cut1 + 1
        return 0.0


# --- TEST ---
sol70 = Solution70()
print(sol70.findMedianSortedArrays([1,3], [2]))       # Expected: 2.0
print(sol70.findMedianSortedArrays([1,2], [3,4]))     # Expected: 2.5
