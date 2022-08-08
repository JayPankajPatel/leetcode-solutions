# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        serial = []
        
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            serial.append(node.val)
            dfs(node.right)
            
            return
        
        dfs(root)
        print(serial)
        return serial[k-1]