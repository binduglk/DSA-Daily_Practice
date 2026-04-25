# Pattern: Fixed Sliding Window
# Time: O(n) | Space: O(1)

def max_sum_subarray(nums, k):
    # Build first window
    window_sum = sum(nums[:k])
    max_sum = window_sum
    print(f"Initial window: {nums[:k]} → sum={window_sum}")

    for i in range(k, len(nums)):
        # Slide: add new element, drop oldest
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)
        print(f"i={i}: +{nums[i]} -{nums[i-k]} → sum={window_sum}, max={max_sum}")

    return max_sum


# ============================
# 🔍 Testing
# ============================

print("Answer:", max_sum_subarray([2, 1, 5, 1, 3, 2], 3))
# Expected trace:
# Initial window: [2,1,5] → sum=8
# i=3: +1 -2 → sum=7
# i=4: +3 -1 → sum=9 ← max
# i=5: +2 -5 → sum=6
# Answer: 9
