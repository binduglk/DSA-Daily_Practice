class ListNode:
    def __init__(self, val=0):   # fixed constructor
        self.val = val
        self.next = None

class Solution:
    def removeCycle(self, head):
        slow = head
        fast = head

        # Step 1: Detect cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            print(f"Step 1 -> Slow at: {slow.val}, Fast at: {fast.val}")

            if slow == fast:
                print("Meeting point found at:", slow.val)
                break
        else:
            print("No cycle detected.")
            return head  # No cycle

        # Step 2: Find start of cycle
        slow = head
        prev = None
        while slow != fast:
            prev = fast
            print(f"Step 2 -> Slow at: {slow.val}, Fast at: {fast.val}")
            slow = slow.next
            fast = fast.next

        # Step 3: Break the cycle
        print("Cycle starts at node with value:", slow.val)
        print("Breaking cycle at node with value:", prev.val)
        prev.next = None

        return head


# -------- Test Code --------
# Create nodes
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

# Link nodes with a cycle
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2   # cycle back to node2

sol = Solution()
head_after_removal = sol.removeCycle(node1)

# Verify by traversing list (should stop, no infinite loop)
print("\nTraversing list after cycle removal:")
curr = head_after_removal
while curr:
    print(curr.val, end=" -> ")
    curr = curr.next