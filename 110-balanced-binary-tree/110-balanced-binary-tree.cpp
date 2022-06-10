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
    std::pair<int, bool> maxHeight(TreeNode* &root) {
        
        if(!root)
            return {0, true}; 
        std::pair<int, bool> left  {maxHeight(root -> left)};
        std::pair<int, bool> right {maxHeight(root -> right)};
        
        bool balanced = left.second && right.second && std::abs(left.first - right.first) <= 1; 

        return {1 + std::max(left.first, right.first), balanced}; 
    }
public:
    bool isBalanced(TreeNode* root) {
        return maxHeight(root).second; 
    }
};