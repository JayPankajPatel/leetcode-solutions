"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldmapnew = {}
        
        def dfs(root):
            if not root:
                return None
            if root in oldmapnew:
                return oldmapnew[root]
            
            cp_node = Node(root.val)
            oldmapnew[root] = cp_node
            for neighbor in root.neighbors:
                cp_node.neighbors.append(dfs(neighbor))
            return cp_node
        return dfs(node)