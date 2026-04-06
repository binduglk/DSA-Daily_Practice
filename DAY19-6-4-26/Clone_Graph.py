# Session 4 - Clone Graph
# LeetCode #133
# Topic - Graph Cloning
# Question - Clone an Undirected Graph
# Day 16

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors else []

class Solution:
    def cloneGraph(self, node: Node) -> Node:
        if not node:
            return None

        cloned = {}    # original → clone mapping

        from collections import deque
        queue = deque([node])
        cloned[node] = Node(node.val)
        print(f"Cloned node {node.val}")

        while queue:
            curr = queue.popleft()
            print(f"Visiting node {curr.val}")

            for neighbor in curr.neighbors:
                if neighbor not in cloned:
                    cloned[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                    print(f"Cloned neighbor {neighbor.val} of node {curr.val}")

                cloned[curr].neighbors.append(cloned[neighbor])
                print(f"Linked {curr.val} → {neighbor.val}")

        return cloned[node]


# Testing
# Graph: 1 -- 2
#        |    |
#        4 -- 3
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

n1.neighbors = [n2, n4]
n2.neighbors = [n1, n3]
n3.neighbors = [n2, n4]
n4.neighbors = [n1, n3]

sol = Solution()
cloned_graph = sol.cloneGraph(n1)

# Print cloned graph structure
def print_graph(node, visited=set()):
    if node in visited:
        return
    visited.add(node)
    print(f"Node {node.val} neighbors: {[n.val for n in node.neighbors]}")
    for neighbor in node.neighbors:
        print_graph(neighbor, visited)

print("\nCloned Graph Structure:")
print_graph(cloned_graph)