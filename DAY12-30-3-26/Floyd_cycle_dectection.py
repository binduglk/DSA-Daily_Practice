# Session 3 - Linked List Cycle
# LeetCode #141
# Topic - Floyd's Cycle Detection
# Day 10

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next          # 1 step
            fast = fast.next.next     # 2 steps

            if slow == fast:          # met! cycle exists!
                return True

        return False                  # no cycle!

# Testing
# No cycle
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
sol = Solution()
print(sol.hasCycle(head))    # False

# With cycle
head2 = ListNode(1)
head2.next = ListNode(2)
head2.next.next = ListNode(3)
head2.next.next.next = head2.next  # cycle!
print(sol.hasCycle(head2))   # True
