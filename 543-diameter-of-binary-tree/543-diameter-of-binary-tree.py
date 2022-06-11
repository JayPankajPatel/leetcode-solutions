# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root: TreeNode) -> int:
        if(not root):
            return 0
        left = self.dfs(root.left) + 1
        right = self.dfs(root.right) + 1
        
        return max(left, right)
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if(not root):
            return 0
        
        op1 = self.dfs(root.left) + self.dfs(root.right)
        op2 = self.diameterOfBinaryTree(root.left)
        op3 = self.diameterOfBinaryTree(root.right)
        
        
        return max(op1, max(op2,op3))