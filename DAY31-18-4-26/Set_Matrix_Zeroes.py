# PROBLEM 24: Set Matrix Zeroes
# LeetCode 73
# Question: Given an m x n integer matrix, if an element is 0, 
# set its entire row and column to 0. Do it in-place.
# ============================================================

class Solution24:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        Key insight:
          - matrix[i][0] = 0 means row i should be zeroed
          - matrix[0][j] = 0 means col j should be zeroed
          - matrix[0][0] is shared → use separate flag 'col0'
            to track whether the first column itself needs zeroing
        """
        rows = len(matrix)
        cols = len(matrix[0])
        col0 = False                                # flag for first column

        print("Initial matrix:", matrix)

        # Step 1: mark first row and first column as flags
        for i in range(rows):
            if matrix[i][0] == 0:
                col0 = True                         # first col needs zeroing
                print(f"Row {i} has 0 in first column → col0=True")
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0               # mark row
                    matrix[0][j] = 0               # mark col
                    print(f"Found 0 at ({i},{j}) → mark row {i} and col {j}")

        print("After marking:", matrix, "col0 =", col0)

        # Step 2: zero inner cells based on markers (bottom-right → top-left)
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, 0, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    print(f"Zeroing cell ({i},{j}) due to marker")
                    matrix[i][j] = 0

        # Step 3: zero first column if flagged
        if col0:
            for i in range(rows):
                print(f"Zeroing first column at row {i}")
                matrix[i][0] = 0

        print("Final matrix:", matrix)

# Testing
sol = Solution24()
mat = [[1,1,1],[1,0,1],[1,1,1]]
sol.setZeroes(mat)
print("Answer:", mat)   # Expected [[1,0,1],[0,0,0],[1,0,1]]

mat2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
sol.setZeroes(mat2)
print("Answer:", mat2)  # Expected [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
