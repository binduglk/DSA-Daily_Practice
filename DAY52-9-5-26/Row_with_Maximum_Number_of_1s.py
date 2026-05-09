'''Problem : Row with Maximum Number of 1s
Platform: GeeksForGeeks
Question:  
Given a binary matrix where each row is sorted (all 0s then 1s), find the row index with the maximum number of 1s.
Approach:
For each row, use binary search (lower bound) to find the first index of 1.
Count of 1s = n - first_one_index.
Track the row with the maximum count.
Time: O(m log n), Space: O(1).'''

class Solution74:
    def rowWithMax1s(self, matrix: list[list[int]]) -> int:
        max_count = 0
        best_row = -1

        for i, row in enumerate(matrix):
            first_one = self._lowerBound(row, 1)
            count = len(row) - first_one
            if count > max_count:
                max_count = count
                best_row = i
        return best_row

    def _lowerBound(self, row: list[int], target: int) -> int:
        low, high = 0, len(row) - 1
        ans = len(row)
        while low <= high:
            mid = low + (high - low) // 2
            if row[mid] >= target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

matrix = [[0,1,1,1],[0,0,1,1],[1,1,1,1],[0,0,0,0]]
print(Solution74().rowWithMax1s(matrix))  # 2
