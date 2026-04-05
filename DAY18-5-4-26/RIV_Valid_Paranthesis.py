'''(LeetCode #20) - valid paranthesis
Given a string s containing just the characters '(', ')', '{', '}', '[', and ']', determine if the input string is valid.
An input string is valid if:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
- Every closing bracket has a corresponding opening bracket of the same type.
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            print(f"Processing: {char}")
            if char in mapping:              # closing bracket
                if not stack:
                    print("Stack empty when expecting match → invalid")
                    return False
                top = stack.pop()
                print(f"Popped from stack: {top}")
                if top != mapping[char]:
                    print(f"Mismatch! Expected {mapping[char]}, got {top}")
                    return False
            else:
                stack.append(char)           # opening bracket
                print(f"Pushed to stack: {char}")

        print(f"Final stack: {stack}")
        return len(stack) == 0


# Testing
sol = Solution()
print("Result:", sol.isValid("()"))        # True
print("Result:", sol.isValid("()[]{}"))    # True
print("Result:", sol.isValid("(]"))        # False
print("Result:", sol.isValid("([)]"))      # False
print("Result:", sol.isValid("{[]}"))      # True

