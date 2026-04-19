# PROBLEM 26: Spiral Matrix
# LeetCode 54
# Question: Given an m x n matrix, return all elements of the matrix in spiral order.
# ============================================================

class Solution26:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        result = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        print("Initial matrix:", matrix)

        while top <= bottom and left <= right:
            print(f"Bounds → top={top}, bottom={bottom}, left={left}, right={right}")

            # Move right along top row
            for col in range(left, right + 1):
                result.append(matrix[top][col])
                print(f"   Right move: Added {matrix[top][col]} at ({top},{col})")
            top += 1

            # Move down along right column
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
                print(f"   Down move: Added {matrix[row][right]} at ({row},{right})")
            right -= 1

            # Move left along bottom row (only if rows remain)
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                    print(f"   Left move: Added {matrix[bottom][col]} at ({bottom},{col})")
                bottom -= 1

            # Move up along left column (only if columns remain)
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                    print(f"   Up move: Added {matrix[row][left]} at ({row},{left})")
                left += 1

        print("Final spiral order:", result)
        return result

# Testing
sol = Solution26()
print("Answer:", sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))  
# Expected [1,2,3,6,9,8,7,4,5]

print("Answer:", sol.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))  
# Expected [1,2,3,4,8,12,11,10,9,5,6,7]
