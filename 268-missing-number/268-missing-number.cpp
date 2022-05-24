class Solution {
public:
    int missingNumber(vector<int>& nums) {
        
        int ideal = 0; 
        for(int i = 0; i <= nums.size(); i++)
        {
            ideal ^= i;
        }
        
        int given = 0; 
        
        for(int i = 0; i < nums.size(); i++)
        {
            given ^= nums[i];
        }
        
        
        return ideal ^ given; 
    }
};