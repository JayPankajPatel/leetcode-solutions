class Solution {
private:
    int find_min(std::vector<int>& nums) {
        
        int l = 0; 
        int r = nums.size()-1; 
        int last = nums[r];
        int boundary_index = -1; 
        while(l <= r) {
            int mid = (r + l)/2;
            int value = nums[mid];
            if(value <= last) {
                boundary_index = mid; 
                r = mid - 1;
            }
            else {
                l = mid + 1;
            }
        }
        
        return boundary_index; 
    }
    
    int binary_search(std::vector<int>& nums, int left, int right, int target) {
        
        while(left <= right) {
            
            int mid = (right + left)/2;
            int value = nums[mid];
            
            if(value == target) {
                return mid; 
            }
            else if(value > target) {
                right = mid - 1;
            }
            else {
                left = mid + 1;
            }
        }
        
        return -1; 
    }
public:
    int search(vector<int>& nums, int target) {
        int min_value = find_min(nums);
        int last_value = nums[nums.size()-1];
        if(min_value == 0) {
            return binary_search(nums, 0, nums.size()-1, target);
        }
        
        if(target >= nums[min_value] && target <= last_value){
            return binary_search(nums, min_value, nums.size() - 1, target);
        }
        
        else
            return binary_search(nums, 0, min_value - 1, target);
    }
};