'''(LeetCode #155) - Min Stack
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
'''

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []    # tracks minimums!
        print("Initialized MinStack")

    def push(self, val: int) -> None:
        self.stack.append(val)
        print(f"Pushed {val} onto stack: {self.stack}")
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
            print(f"Updated min_stack: {self.min_stack}")

    def pop(self) -> None:
        top = self.stack.pop()
        print(f"Popped {top} from stack: {self.stack}")
        if top == self.min_stack[-1]:
            self.min_stack.pop()
            print(f"Updated min_stack after pop: {self.min_stack}")

    def top(self) -> int:
        print(f"Top element is: {self.stack[-1]}")
        return self.stack[-1]

    def getMin(self) -> int:
        print(f"Current minimum is: {self.min_stack[-1]}")
        return self.min_stack[-1]


# Testing
min_stack = MinStack()
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)
print("Min:", min_stack.getMin())   # -3
min_stack.pop()
print("Top:", min_stack.top())      # 0
print("Min:", min_stack.getMin())   # -2