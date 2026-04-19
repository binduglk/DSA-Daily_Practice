# PROBLEM 25: Rotate Image (Matrix 90° Clockwise)
# LeetCode 48
# Question: You are given an n x n 2D matrix representing an image.
# Rotate the image by 90 degrees (clockwise). Do it in-place.
# ============================================================

class Solution25:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        Step 1: Transpose — swap matrix[i][j] with matrix[j][i]
        Step 2: Reverse each row
        """
        n = len(matrix)
        print("Initial matrix:", matrix)

        # Step 1: Transpose (only upper triangle to avoid double-swap)
        for i in range(n):
            for j in range(i + 1, n):
                print(f"Transpose swap: ({i},{j}) <-> ({j},{i})")
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                print("   Current matrix:", matrix)

        # Step 2: Reverse each row
        for idx, row in enumerate(matrix):
            print(f"Reversing row {idx}: before={row}")
            row.reverse()
            print(f"   After={row}")

        print("Final rotated matrix:", matrix)

# Testing
sol = Solution25()
mat = [[1,2,3],[4,5,6],[7,8,9]]
sol.rotate(mat)
print("Answer:", mat)   # Expected [[7,4,1],[8,5,2],[9,6,3]]

mat2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
sol.rotate(mat2)
print("Answer:", mat2)  # Expected [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
