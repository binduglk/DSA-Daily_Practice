# Session 1 - Number of Islands
# LeetCode #200
# Topic - DFS on Grid
# Day 16

class Solution:
    def numIslands(self, grid: list) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        count = 0

        def dfs(r, c):
            # out of bounds or water → stop!
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if grid[r][c] != '1':
                return

            grid[r][c] = '0'    # mark visited!

            # explore all 4 directions
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count += 1
                    print(f"Island found at ({r},{c}), current count = {count}")
                    dfs(r, c)

        return count


# Testing
grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]

sol = Solution()
result = sol.numIslands(grid)
print("Total number of islands:", result)