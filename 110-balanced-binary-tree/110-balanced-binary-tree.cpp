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
    int maxHeight(TreeNode* root) {
        
        if (!root)
            return 0; 
        int left = maxHeight(root -> left) + 1;
        int right = maxHeight(root -> right) + 1;
        
        return std::max(left, right);
    }
public:
    bool isBalanced(TreeNode* root) {
        if(!root)
            return true; 
        int lstree = maxHeight(root -> left);
        int rstree = maxHeight(root -> right);
        
        if(std::abs(lstree - rstree) > 1) 
            return false; 
        
        bool left = isBalanced(root -> left);
        bool right = isBalanced(root -> right);
        
        return left && right; 
    }
};