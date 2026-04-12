# ---- Problem 3: Left Rotate by K ----
# Topic - Array Manipulation (Rotation using Reversal Algorithm)

class Solution3:
    def rotateLeft(self, arr: list[int], k: int) -> list[int]:
        n = len(arr)
        k = k % n   # handle cases where k > n

        print(f"Original array: {arr}")
        print(f"Rotate left by {k} positions")

        def reverse(l, r):
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                print(f"Reversed indices {l} and {r} → {arr}")
                l += 1
                r -= 1

        # Step 1: Reverse first k elements
        print(f"\nStep 1: Reverse first {k} elements")
        reverse(0, k - 1)

        # Step 2: Reverse remaining n-k elements
        print(f"\nStep 2: Reverse remaining {n-k} elements")
        reverse(k, n - 1)

        # Step 3: Reverse entire array
        print(f"\nStep 3: Reverse entire array")
        reverse(0, n - 1)

        print(f"\nFinal rotated array: {arr}")
        return arr


# Testing
nums = [1, 2, 3, 4, 5, 6, 7]
sol = Solution3()
rotated = sol.rotateLeft(nums, 3)
print("Result:", rotated)