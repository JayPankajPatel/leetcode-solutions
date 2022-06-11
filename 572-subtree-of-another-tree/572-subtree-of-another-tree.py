# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if(not root and not subRoot):
            return True
        if(bool(root == None) ^ bool(subRoot == None)):
            return False
        if(root and subRoot and root.val != subRoot.val):
            return False 
        
        return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)
    
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if(not root):
            return False
        if(not subRoot and root):
            return True
      
        if(self.sameTree(root, subRoot)):
            return True
        
        
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)