# LeetCode #206
# Topic - Linked List Reversal
# Day 10
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head

        while curr:
            next_node = curr.next    # save next
            curr.next = prev         # reverse link!
            prev = curr              # move prev
            curr = next_node         # move curr

        return prev

# Helper to print list
def printList(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)

# Testing
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

sol = Solution()
printList(sol.reverseList(head))  # [5,4,3,2,1]