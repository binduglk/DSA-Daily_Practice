# PROBLEM 45: Fruit Into Baskets
# LeetCode 904
# Equivalent: Longest subarray with at most 2 distinct elements
# Approach: Variable sliding window + HashMap (frequency count)
# Time: O(n) | Space: O(1) — map holds at most 3 keys

class Solution45:
    def totalFruit(self, fruits: list[int]) -> int:
        freq = {}
        left = 0
        max_fruits = 0

        for right in range(len(fruits)):
            freq[fruits[right]] = freq.get(fruits[right], 0) + 1

            while len(freq) > 2:
                left_fruit = fruits[left]
                freq[left_fruit] -= 1
                if freq[left_fruit] == 0:
                    del freq[left_fruit]
                left += 1

            max_fruits = max(max_fruits, right - left + 1)

        return max_fruits


# --- TEST ---
sol45 = Solution45()
print(sol45.totalFruit([1,2,1]))                 # Expected: 3
print(sol45.totalFruit([0,1,2,2]))               # Expected: 3
print(sol45.totalFruit([1,2,3,2,2]))             # Expected: 4
print(sol45.totalFruit([3,3,3,1,2,1,1,2,3,3,4])) # Expected: 5
