# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = []
        def dfs(root):
            if not root:
                return
            if root:
                dfs(root.left)
                res.append(root.val)
                dfs(root.right)
            
            return
        dfs(root)
        
        for i in range(len(res)-1):
            if(res[i] >= res[i + 1]):
                return False
            
        return True
             
