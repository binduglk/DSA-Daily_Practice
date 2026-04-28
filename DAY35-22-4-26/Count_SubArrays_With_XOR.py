# PROBLEM 35: Count Subarrays with XOR = k
# Approach: Prefix XOR + HashMap
# Key: if curr_xor ^ prev_xor == k  →  prev_xor == curr_xor ^ k
# Time: O(n) | Space: O(n)
# ============================================================
# Question: Given an array of integers and an integer k, 
# return the number of subarrays whose XOR equals k.

class Solution35:
    def countSubarraysXOR(self, arr: list[int], k: int) -> int:
        xor_map = {0: 1}        # XOR value 0 seen once before array starts
        curr_xor = 0
        count = 0

        for val in arr:
            curr_xor ^= val     # running XOR with current element

            # how many previous prefix XORs satisfy: prev == curr_xor ^ k
            needed = curr_xor ^ k
            if needed in xor_map:
                count += xor_map[needed]

            # record current prefix XOR
            xor_map[curr_xor] = xor_map.get(curr_xor, 0) + 1

        return count


# ============================
# 🔍 Testing
# ============================

sol = Solution35()

print("Test 1:", sol.countSubarraysXOR([4,2,2,6,4], 6))
# Expected: 4 → subarrays are [4,2], [6], [2,2,6], [4,2,2,6,4]

print("Test 2:", sol.countSubarraysXOR([5,6,7,8,9], 5))
# Expected: 2 → subarrays are [5], [6,7,8,9]

print("Test 3:", sol.countSubarraysXOR([1,2,3,4], 6))
# Expected: 2 → subarrays are [2,4], [1,2,3]

print("Test 4:", sol.countSubarraysXOR([10,10,10], 0))
# Expected: 2 → subarrays are [10,10], [10,10,10]

print("Test 5:", sol.countSubarraysXOR([1,1,1,1], 1))
# Expected: 4 → each single-element subarray [1]
