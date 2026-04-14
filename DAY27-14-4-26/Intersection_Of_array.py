# LeetCode Question: 349. Intersection of Two Arrays
# Problem: Given two arrays, return their intersection (unique elements only).
# Time Complexity: O(m log m + n log n) due to sorting
# Space Complexity: O(1) excluding output storage

def intersection(nums1, nums2):
    i, j = 0, 0
    result = []
    nums1.sort()
    nums2.sort()
    
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            if not result or result[-1] != nums1[i]:
                result.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1
    
    return result

# Example usage
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print("Intersection:", intersection(nums1, nums2))