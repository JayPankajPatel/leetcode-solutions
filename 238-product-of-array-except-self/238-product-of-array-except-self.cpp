class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        std::vector<int> ans(nums.size(),1);
    
        
       for(int i = 1; i < nums.size(); i++)
       {
           ans[i] = ans[i-1] * nums[i-1]; 
       }
        
        int product = 1;
        
       for(int i = nums.size()-2; i >= 0; i--){
           product*=nums[i+1];
           ans[i] *= product;
           
       }
        
        return ans; 
    }
};