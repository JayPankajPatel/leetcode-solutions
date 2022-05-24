class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        
        std::unordered_set<int> our_set(nums.begin(),nums.end());
        
        return nums.size() != our_set.size();
    }
};