# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = [[root.val]]
        
        queue = deque()
        queue.append(root)
        
        while(queue):
            n = len(queue)
            loop_res = []
            for i in range(n):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    loop_res.append(node.left.val)
                if node.right:
                    queue.append(node.right)
                    loop_res.append(node.right.val)
                
            res.append(loop_res)
        
        res.pop()
        return res
                    
                
        