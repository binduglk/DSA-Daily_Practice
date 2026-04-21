# PROBLEM 31: Count Frequency of Each Element
# Approach: HashMap frequency counter
# Time: O(n) | Space: O(n)
# ============================================================
# Question: Given an array of integers, count the frequency of each element.
# Also find the element with the highest frequency and the element with the lowest frequency.

class Solution31:
    def countFrequency(self, arr: list[int]) -> dict:
        freq = {}
        for num in arr:
            # if key exists add 1, else start at 1
            freq[num] = freq.get(num, 0) + 1
        return freq

    def highestLowestFreq(self, arr: list[int]) -> tuple:
        freq = self.countFrequency(arr)

        max_count = max(freq.values())
        min_count = min(freq.values())

        max_elem = [k for k, v in freq.items() if v == max_count][0]
        min_elem = [k for k, v in freq.items() if v == min_count][0]

        return max_elem, min_elem


# ============================
# 🔍 Testing
# ============================

sol = Solution31()

print("Test 1:", sol.countFrequency([1,2,2,3,3,3,4]))
# Expected: {1:1, 2:2, 3:3, 4:1}
print("Highest & Lowest:", sol.highestLowestFreq([1,2,2,3,3,3,4]))
# Expected: (3,1) → 3 occurs most, 1 occurs least

print("Test 2:", sol.countFrequency([5,5,5,6,6,7]))
# Expected: {5:3, 6:2, 7:1}
print("Highest & Lowest:", sol.highestLowestFreq([5,5,5,6,6,7]))
# Expected: (5,7)

print("Test 3:", sol.countFrequency([10,10,20,30,30,30,40,40]))
# Expected: {10:2, 20:1, 30:3, 40:2}
print("Highest & Lowest:", sol.highestLowestFreq([10,10,20,30,30,30,40,40]))
# Expected: (30,20)

print("Test 4:", sol.countFrequency([1]))
# Expected: {1:1}
print("Highest & Lowest:", sol.highestLowestFreq([1]))
# Expected: (1,1)
