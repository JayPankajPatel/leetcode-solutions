# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = []
        
        def dfs(root):
            if(root):
                dfs(root.left)
                print(root.val)
                arr.append(root.val)
                dfs(root.right)
            
            return
        dfs(root)
        
        for i in range(1, len(arr)):
            if(arr[i] <= arr[i-1]):
                return False
        return True