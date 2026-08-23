"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node: return None
        cloned = [Node(i + 1) for i in range(100)]
        visited = set()

        def dfs(node):
            visited.add(node)
            new_node = cloned[node.val-1]
            print(node.val)
            for neigh in node.neighbors:
                new_neigh = cloned[neigh.val-1]
                if new_neigh not in new_node.neighbors:
                    new_node.neighbors.append(new_neigh)

                if new_node not in new_neigh.neighbors:
                    new_neigh.neighbors.append(new_node)
                if neigh not in visited:
                    dfs(neigh)

        dfs(node)
        return cloned[0]
