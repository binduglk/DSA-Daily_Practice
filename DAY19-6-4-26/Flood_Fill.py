# Session 2 - Flood Fill
# LeetCode #733
# Topic - DFS on Grid
# Day 16

class Solution:
    def floodFill(self, image: list,
                  sr: int, sc: int,
                  color: int) -> list:

        original = image[sr][sc]

        # if already same color → no change!
        if original == color:
            return image

        def dfs(r, c):
            if r < 0 or r >= len(image):
                return
            if c < 0 or c >= len(image[0]):
                return
            if image[r][c] != original:
                return

            image[r][c] = color    # fill!
            print(f"Filled pixel ({r},{c}) with color {color}")

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        dfs(sr, sc)
        return image


# Testing
image = [
    [1,1,1],
    [1,1,0],
    [1,0,1]
]

sol = Solution()
result = sol.floodFill(image, 1, 1, 2)

print("Final filled image:")
for row in result:
    print(row)