class Solution15:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}                                # num → index
        print("Initial seen =", seen)

        for i, num in enumerate(nums):
            complement = target - num            # what we need to find
            print(f"Index={i}, Num={num}, Complement={complement}")

            if complement in seen:
                print(f"   Found complement {complement} in seen at index {seen[complement]}")
                return [seen[complement], i]     # found the pair

            seen[num] = i                        # store current number
            print(f"   Updated seen = {seen}")

        print("No solution found")
        return []                                # no solution (won't reach here per problem)

# Testing
sol = Solution15()
print("Answer:", sol.twoSum([2,7,11,15], 9))   # Expected [0,1]
print("Answer:", sol.twoSum([3,2,4], 6))       # Expected [1,2]
print("Answer:", sol.twoSum([3,3], 6))         # Expected [0,1]