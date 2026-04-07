# Session - Permutations
# LeetCode #46
# Topic - Backtracking
# Question - Generate all permutations of a list
# Day XX

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []

        def backtrack(path, used):
            if len(path) == len(nums):
                result.append(path[:])
                print(f"Added permutation: {path}")
                return

            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])
                print(f"Choose {nums[i]} → {path}")
                backtrack(path, used)
                path.pop()
                used[i] = False
                print(f"Backtrack, remove {nums[i]} → {path}")

        backtrack([], [False] * len(nums))
        return result


# Testing
nums = [1, 2, 3]
sol = Solution()
permutations_result = sol.permute(nums)

print("\nAll permutations:")
for perm in permutations_result:
    print(perm)