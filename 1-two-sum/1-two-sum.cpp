class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        std::unordered_map<int,int> our_map; 
        std::vector<int> ans; 
        
        for(int i = 0; i < nums.size(); i++)
        {
            if(our_map.find(target-nums[i]) != our_map.end())
            {
                ans.push_back(our_map[target-nums[i]]);
                ans.push_back(i);
            }
            
            our_map[nums[i]] = i; 
        }
        
        return ans; 
    }
};