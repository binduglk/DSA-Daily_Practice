# PROBLEM 27: Subarray Sum Equals K
# LeetCode 560
# Question: Given an integer array nums and an integer k, 
# return the total number of subarrays whose sum equals k.
# ============================================================

class Solution27:
    def subarraySum(self, nums: list[int], k: int) -> int:
        # prefix_map stores {prefix_sum: how many times it has occurred}
        prefix_map = {0: 1}     # empty subarray has prefix sum 0
        running_sum = 0
        count = 0

        print("Initial prefix_map:", prefix_map)

        for i, num in enumerate(nums):
            running_sum += num
            needed = running_sum - k

            print(f"Index={i}, Num={num}, RunningSum={running_sum}, Needed={needed}")

            # if (running_sum - k) exists in map,
            # those are valid starting points for subarrays ending here
            if needed in prefix_map:
                count += prefix_map[needed]
                print(f"   Found {needed} in prefix_map → add {prefix_map[needed]} to count → count={count}")

            # record current prefix sum in map
            prefix_map[running_sum] = prefix_map.get(running_sum, 0) + 1
            print(f"   Updated prefix_map: {prefix_map}")

        print("Final count =", count)
        return count

# Testing
sol = Solution27()
print("Answer:", sol.subarraySum([1,1,1], 2))          # Expected 2
print("Answer:", sol.subarraySum([1,2,3], 3))          # Expected 2 ([1,2], [3])
print("Answer:", sol.subarraySum([3,4,7,-2,2,1,4,2], 7)) # Expected 4
