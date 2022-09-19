"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        from collections import defaultdict
        visited = defaultdict(List)
        
        def dfs(node):
            nonlocal visited
            if node in visited:
                return visited[node]
            
            cp = Node(node.val)
            visited[node] = cp
            for neighbor in node.neighbors:
                cp.neighbors.append(dfs(neighbor))
            return cp
        
        return dfs(node) if node else None
            
            
            