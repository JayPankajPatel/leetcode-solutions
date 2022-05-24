/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
private: 
    int dfs(TreeNode* root) {
        
        if(!root)
            return 0; 
        
        int left = dfs(root -> left) + 1;
        int right = dfs(root -> right) + 1;
        
        return max(left, right); 
    }
public:
    int diameterOfBinaryTree(TreeNode* root) {
        
        if(!root)
            return 0; 
        
        int op1 = dfs(root -> left) + dfs(root -> right);
        int op2 = diameterOfBinaryTree(root -> left);
        int op3 = diameterOfBinaryTree(root -> right);
        
        
        return std::max(op1, std::max(op2, op3)); 
        
    }
};