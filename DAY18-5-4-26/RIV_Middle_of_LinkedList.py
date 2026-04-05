# Session 2 - Middle of Linked List
# LeetCode #876
# Topic - Slow/Fast Pointer
# Day 10

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next          # 1 step
            fast = fast.next.next     # 2 steps

        return slow

# Testing
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

sol = Solution()
print(sol.middleNode(head).val)   # 3