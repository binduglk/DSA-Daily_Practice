# PROBLEM 32: Find ALL Elements with Highest and Lowest Frequency
# Approach: Frequency map → group by count
# Time: O(n) | Space: O(n)
# ============================================================
# Question: Given an array of integers, count the frequency of each element.
# Return ALL elements that share the highest frequency and ALL elements that share the lowest frequency.

class Solution32:
    def highestLowestFreqAll(self, arr: list[int]) -> tuple:
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1

        max_count = max(freq.values())
        min_count = min(freq.values())

        # collect ALL elements sharing the max/min frequency
        highest = [k for k, v in freq.items() if v == max_count]
        lowest  = [k for k, v in freq.items() if v == min_count]

        return sorted(highest), sorted(lowest)


# ============================
# 🔍 Testing
# ============================

sol = Solution32()

print("Test 1:", sol.highestLowestFreqAll([1,2,2,3,3,3,4]))
# Expected: ([3], [1,4]) → 3 occurs most, 1 and 4 occur least

print("Test 2:", sol.highestLowestFreqAll([5,5,5,6,6,7]))
# Expected: ([5], [7]) → 5 occurs most, 7 occurs least

print("Test 3:", sol.highestLowestFreqAll([10,10,20,30,30,30,40,40]))
# Expected: ([30], [20]) → 30 occurs most, 20 occurs least

print("Test 4:", sol.highestLowestFreqAll([1,2,3,4]))
# Expected: ([1,2,3,4], [1,2,3,4]) → all occur once, so both highest and lowest are all elements

print("Test 5:", sol.highestLowestFreqAll([7,7,8,8,9,9,10]))
# Expected: ([7,8,9], [10]) → 7,8,9 occur twice, 10 occurs once
