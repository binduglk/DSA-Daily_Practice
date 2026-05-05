# P45: Fruit Into Baskets
# LeetCode 904
# Problem: You have 2 baskets, each can hold only 1 type of fruit.
# Find the length of the longest subarray with at most 2 distinct values.
# ============================================================
# Pattern: Variable window + frequency hashmap
# Time: O(n) | Space: O(1) — at most 3 keys ever
# "At most 2 distinct types" → shrink when distinct > 2

def total_fruit(fruits: list[int]) -> int:
    basket = {}  # fruit_type → count in window
    left = 0
    max_len = 0

    for right in range(len(fruits)):
        fruit = fruits[right]
        basket[fruit] = basket.get(fruit, 0) + 1

        # Window invalid: more than 2 types → shrink
        while len(basket) > 2:
            left_fruit = fruits[left]
            basket[left_fruit] -= 1
            if basket[left_fruit] == 0:
                del basket[left_fruit]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len


# ============================
# 🔍 Testing
# ============================

print("Test 1:", total_fruit([1,2,1]))
# Expected: 3 → whole array [1,2,1]

print("Test 2:", total_fruit([0,1,2,2]))
# Expected: 3 → subarray [1,2,2]

print("Test 3:", total_fruit([1,2,3,2,2]))
# Expected: 4 → subarray [2,3,2,2]

print("Test 4:", total_fruit([3,3,3,1,2,1,1,2,3,3,4]))
# Expected: 5 → subarray [1,2,1,1,2]

print("Test 5:", total_fruit([1,2,1,2,1,2,1]))
# Expected: 7 → whole array (only 2 types)
