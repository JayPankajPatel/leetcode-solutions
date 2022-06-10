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
    int dfs(TreeNode* root, int maxsf) {
        
        if(!root)
            return 0; 
        int total = 0; 
        if(root -> val  >= maxsf) {
            total++; 
            maxsf = root -> val; 
        }
        
        total += dfs(root -> left, maxsf);
        total += dfs(root -> right, maxsf);
        
        return total; 
    }
public:
    int goodNodes(TreeNode* root) {
        
        return dfs(root, std::numeric_limits<int>::min()); 
    }
};