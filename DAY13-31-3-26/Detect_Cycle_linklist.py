# Detect Cycle in Linked List

class ListNode:
    def __init__(self, val=0):   # <-- double underscores
        self.val = val
        self.next = None


class Solution:
    def hasCycle(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            print(f"Slow at node with value: {slow.val}")
            print(f"Fast at node with value: {fast.val}")

            if slow == fast:
                print("Cycle detected!")
                return True

        return False

        print("No cycle found.")
        return False

# -------- Test Code --------
# Create nodes
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

# Link nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2   # creates a cycle back to node2

# Run detection
sol = Solution()
print("Has cycle?", sol.hasCycle(node1))
