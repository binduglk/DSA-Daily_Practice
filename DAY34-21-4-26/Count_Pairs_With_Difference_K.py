# PROBLEM 33: Count Pairs with Difference K
# Approach: HashSet — for each x, check if x+K exists
# Time: O(n) | Space: O(n)
# ============================================================
# Question: Given an array of integers and an integer k, 
# return the number of unique pairs (x, y) such that y - x = k.

class Solution33:
    def countPairsWithDiffK(self, arr: list[int], k: int) -> int:
        if k < 0:
            return 0

        num_set = set(arr)          # O(1) lookup
        count = 0

        for num in num_set:         # iterate over SET to avoid duplicate pairs
            if num + k in num_set:
                count += 1

        return count


# ============================
# 🔍 Testing
# ============================

sol = Solution33()

print("Test 1:", sol.countPairsWithDiffK([1,2,3,4,5], 2))
# Expected: 3 → pairs are (1,3), (2,4), (3,5)

print("Test 2:", sol.countPairsWithDiffK([1,5,3,4,2], 2))
# Expected: 3 → pairs are (1,3), (3,5), (2,4)

print("Test 3:", sol.countPairsWithDiffK([8,12,16,4,0], 4))
# Expected: 4 → pairs are (0,4), (4,8), (8,12), (12,16)

print("Test 4:", sol.countPairsWithDiffK([1,1,1,1], 0))
# Expected: 1 → only one unique pair (1,1)

print("Test 5:", sol.countPairsWithDiffK([10,20,30,40,50], 10))
# Expected: 4 → pairs are (10,20), (20,30), (30,40), (40,50)
