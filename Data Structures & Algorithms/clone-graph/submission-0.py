"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        maps = {}
        if not node: 
            return None
        def dfs(node):
            if node in maps:
                return maps[node]
            copy = Node(node.val)
            maps[node] = copy
            for nodes in node.neighbors:
                copy.neighbors.append(dfs(nodes))
            return copy
        return dfs(node)
