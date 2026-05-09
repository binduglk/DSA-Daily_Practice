'''Problem : Search in a 2D Matrix II
Platform: LeetCode 240
Question:  
Given an m x n matrix where each row is sorted left→right and each column is sorted top→bottom, determine if a target value exists in the matrix.
Approach:
Start from the top-right corner.
If current value == target → return True.
If current value > target → move left (eliminate column).
If current value < target → move down (eliminate row).
Time: O(m+n), Space: O(1).'''

class Solution73:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix:
            return False

        rows, cols = len(matrix), len(matrix[0])
        row, col = 0, cols - 1

        while row < rows and col >= 0:
            val = matrix[row][col]
            if val == target:
                return True
            elif val > target:
                col -= 1
            else:
                row += 1
        return False

matrix = [[1,4,7],[2,5,8],[3,6,9]]
print(Solution73().searchMatrix(matrix, 5))  # True
print(Solution73().searchMatrix(matrix, 10)) # False
