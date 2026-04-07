# Session - Subsets
# LeetCode #78
# Topic - Backtracking / Power Set


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []

        def backtrack(start, path):
            # add current subset
            result.append(path[:])
            print(f"Added subset: {path}")

            # explore further elements
            for i in range(start, len(nums)):
                path.append(nums[i])
                print(f"Include {nums[i]} → {path}")
                backtrack(i + 1, path)
                path.pop()
                print(f"Backtrack, remove {nums[i]} → {path}")

        backtrack(0, [])
        return result


# Testing
nums = [1, 2, 3]
sol = Solution()
subsets_result = sol.subsets(nums)

print("\nAll subsets:")
for subset in subsets_result:
    print(subset)