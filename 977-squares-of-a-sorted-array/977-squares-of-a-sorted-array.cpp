class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        std::vector<int> res;
        
        int left = 0; 
        int right = nums.size() - 1;
        
        while(left <= right) {
            if(std::abs(nums[left]) > std::abs(nums[right])) {
                res.push_back(nums[left] * nums[left]);
                left++; 
            }
            
            else {
                res.push_back(nums[right] * nums[right]);
                right--;
            }
        }
        
        std::reverse(res.begin(), res.end());
        
        return res; 
    }
};