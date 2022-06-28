# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque
        if not root:
            return []
        queue = deque([root])
        right_side = []
        
        while len(queue) != 0:
            n = len(queue)
            
            for i in range(n):
                node = queue[0]
                if i == n-1:
                    right_side.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                queue.popleft()
            
        return right_side