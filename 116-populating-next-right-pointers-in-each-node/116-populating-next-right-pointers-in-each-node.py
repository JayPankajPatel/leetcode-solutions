"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        def bfs(root):
            if not root.left:
                return 

            if root.right:
                root.left.next = root.right
            if root.next and root.left:
                root.right.next = root.next.left
            else:
                root.next = None
                
            bfs(root.left)
            bfs(root.right)
        
        bfs(root)
        
        return root
        