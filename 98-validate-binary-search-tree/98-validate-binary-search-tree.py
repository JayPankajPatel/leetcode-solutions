# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.res = []
        def dfs(root):
            if not root:
                return 
            if root: 
                dfs(root.left)
                self.res.append(root.val)
                dfs(root.right)
            
        dfs(root)
        
        for i in range(len(self.res) -1):
            if self.res[i] >= self.res[i + 1]:
                return False
        
        return True
                
        