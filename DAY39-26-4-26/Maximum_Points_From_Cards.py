# P47: Maximum Points You Can Obtain from Cards
# LeetCode 1423
# Pattern: Fixed window (inverse thinking)
# Key insight: taking k cards from ends = leaving n-k cards in the middle
# Maximize end sum = Minimize middle window sum
# Time: O(n) | Space: O(1)

class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        n = len(cardPoints)
        window_size = n - k        # size of middle portion to MINIMIZE

        # Edge case: take all cards
        if window_size == 0:
            return sum(cardPoints)

        # Build first window (leftmost n-k elements)
        window_sum = sum(cardPoints[:window_size])
        min_window = window_sum
        total = sum(cardPoints)

        # Slide window across the array
        for i in range(window_size, n):
            window_sum += cardPoints[i] - cardPoints[i - window_size]
            min_window = min(min_window, window_sum)

        return total - min_window


# ============================
# 🔍 Testing
# ============================

sol = Solution()

print("Test 1:", sol.maxScore([1, 2, 3, 4, 5, 6, 1], 3))
# Expected: 12 → best pick is [1,6,5]

print("Test 2:", sol.maxScore([2, 2, 2], 2))
# Expected: 4 → pick any two cards

print("Test 3:", sol.maxScore([9, 7, 7, 9, 7, 7, 9], 7))
# Expected: 55 → take all cards

print("Test 4:", sol.maxScore([1, 1000, 1], 1))
# Expected: 1 → best pick is either edge card

print("Test 5:", sol.maxScore([11,49,100,20,86,29,72], 4))
# Expected: 232 → optimal pick from both ends
