'''PROBLEM : Search in a 2D Matrix
LeetCode 74
Problem: Given an m x n matrix where each row is sorted and the first element of each row is greater than the last of the previous row, determine if target exists.
Approach: Treat as one sorted array of m*n elements. Binary search with index mapping.
Time: O(log(m*n)) | Space: O(1)'''

class Solution72:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        low, high = 0, m * n - 1

        while low <= high:
            mid = low + (high - low) // 2
            row, col = mid // n, mid % n
            val = matrix[row][col]

            if val == target:
                return True
            elif val < target:
                low = mid + 1
            else:
                high = mid - 1
        return False


# --- TEST ---
sol72 = Solution72()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
print(sol72.searchMatrix(matrix, 3))   # Expected: True
print(sol72.searchMatrix(matrix, 13))  # Expected: False
