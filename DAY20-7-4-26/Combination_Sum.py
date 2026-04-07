# Session - Combination Sum
# LeetCode #39
# Topic - Backtracking
# Question - Find all combinations that sum to target

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []

        def backtrack(start, path, total):
            if total == target:
                result.append(path[:])
                print(f"Found combination: {path}")
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                print(f"Choose {candidates[i]} → {path}, total = {total + candidates[i]}")
                backtrack(i, path, total + candidates[i])  # reuse allowed
                path.pop()
                print(f"Backtrack, remove {candidates[i]} → {path}, total = {total}")

        backtrack(0, [], 0)
        return result


# Testing
candidates = [2, 3, 6, 7]
target = 7
sol = Solution()
combinations_result = sol.combinationSum(candidates, target)

print("\nAll combinations:")
for combo in combinations_result:
    print(combo)