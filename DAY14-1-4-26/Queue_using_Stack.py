''' (LeetCode #232) -   Queue using Stack
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue:
'''

class MyQueue:
    def __init__(self):
        self.stack1 = []    # for push
        self.stack2 = []    # for pop
        print("Initialized MyQueue")

    def push(self, x: int) -> None:
        self.stack1.append(x)
        print(f"Pushed {x} into stack1: {self.stack1}")

    def pop(self) -> int:
        if not self.stack2:
            print("stack2 empty → transferring from stack1")
            while self.stack1:
                moved = self.stack1.pop()
                self.stack2.append(moved)
                print(f"Moved {moved} from stack1 to stack2")
        val = self.stack2.pop()
        print(f"Popped {val} from stack2: {self.stack2}")
        return val

    def peek(self) -> int:
        if not self.stack2:
            print("stack2 empty → transferring from stack1 for peek")
            while self.stack1:
                moved = self.stack1.pop()
                self.stack2.append(moved)
                print(f"Moved {moved} from stack1 to stack2")
        print(f"Front element is: {self.stack2[-1]}")
        return self.stack2[-1]

    def empty(self) -> bool:
        is_empty = not self.stack1 and not self.stack2
        print(f"Queue empty? {is_empty}")
        return is_empty


# Testing
q = MyQueue()
q.push(1)
q.push(2)
print("Peek:", q.peek())   # 1
print("Pop:", q.pop())     # 1
print("Empty?", q.empty()) # False