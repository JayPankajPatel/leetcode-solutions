class Solution {
public:
    int findMin(vector<int>& nums) {
        int left = 0; 
        int right = nums.size() -1;
        int boundary_index = -1; 
        int last = nums[right];
        while (left <= right) {
            
            int mid = (right + left) / 2; 
            
            if(last >= nums[mid]) {
                boundary_index = mid; 
                right = mid - 1;
            }
            else
                left = mid + 1;
        }
        
        
        return nums[boundary_index]; 
    }
};