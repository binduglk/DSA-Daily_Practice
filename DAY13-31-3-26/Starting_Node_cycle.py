# Find Starting Node of Cycle


class ListNode:
    def __init__(self, val=0):   # fixed constructor
        self.val = val
        self.next = None



class Solution:
    def detectCycle(self, head):
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
            return None   # No cycle

        # Step 2: Find start node
        slow = head
        while slow != fast:
            print(f"Step 2 -> Slow at: {slow.val}, Fast at: {fast.val}")
            slow = slow.next
            fast = fast.next

        print("Cycle starts at node with value:", slow.val)
        return slow


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
start_node = sol.detectCycle(node1)
print("Returned cycle start node value:", start_node.val if start_node else None)