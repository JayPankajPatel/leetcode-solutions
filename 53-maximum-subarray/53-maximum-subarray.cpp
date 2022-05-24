class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        
        int max_sofar = -10001; 
        
        int max_tol = -10001; 
        
        
        for(const int& x : nums)
        {
            max_sofar = max(x, max_sofar + x); 
            
            max_tol = max(max_tol, max_sofar); 
        }
        
        return max_tol; 
    }
};