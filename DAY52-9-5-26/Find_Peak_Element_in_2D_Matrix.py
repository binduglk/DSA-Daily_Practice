'''Problem : Find Peak Element in 2D Matrix
Platform: LeetCode 1901
Question:  
Find a peak element in a 2D matrix. A peak is defined as an element strictly greater than its four neighbors (up, down, left, right).

Approach:
Perform binary search on columns.
For each mid column, find the row with the maximum element.
Compare with left and right neighbors.
If greater → peak found.
Else move search to left or right half.
Time: O(m log n), Space: O(1).'''

class Solution75:
    def findPeakGrid(self, mat: list[list[int]]) -> list[int]:
        rows, cols = len(mat), len(mat[0])
        low, high = 0, cols - 1

        while low <= high:
            mid_col = low + (high - low) // 2
            max_row = 0
            for r in range(rows):
                if mat[r][mid_col] > mat[max_row][mid_col]:
                    max_row = r

            left  = mat[max_row][mid_col - 1] if mid_col > 0 else -1
            right = mat[max_row][mid_col + 1] if mid_col < cols - 1 else -1

            if mat[max_row][mid_col] > left and mat[max_row][mid_col] > right:
                return [max_row, mid_col]
            elif left > mat[max_row][mid_col]:
                high = mid_col - 1
            else:
                low = mid_col + 1
        return [-1, -1]

matrix = [[1,4],[3,2]]
print(Solution75().findPeakGrid(matrix))  # [1,0]
