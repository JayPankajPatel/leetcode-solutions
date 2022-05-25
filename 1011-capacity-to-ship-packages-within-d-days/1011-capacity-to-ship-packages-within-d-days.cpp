class Solution {
private:
    int sum(std::vector<int>& weights) {
        int sum {0};
        
        for(auto&& x : weights)
            sum += x; 
        
        return sum;  
    }
    
    bool valid(std::vector<int>& weights, int pos_val, int days) {
        int needed_days {1};
        int sum_of_weights{0};
        
        for(auto&& x : weights) {
        
            if(sum_of_weights + x > pos_val) {
               
                sum_of_weights = 0; 
                needed_days++;
            }
            
            if(needed_days > days)
                return false; 
            
            sum_of_weights += x;
        }
        
        return true; 
    }
    
    int max_elem(std::vector<int>& weights) {
        
        int max_val{0};
        
        for(auto&& x : weights)
            max_val = std::max(max_val, x);
        
        return max_val; 
    }
    
public:
    int shipWithinDays(vector<int>& weights, int days) {
        
        int l {max_elem(weights)}; 
        int r {sum(weights)};
        int boundary_index {0};
        
        while(l <= r) {
            
            int mid{(r + l) / 2};
            
            if(valid(weights, mid, days)) {
                boundary_index = mid; 
                r = mid - 1;
            }
            
            else
                l = mid + 1;
        }
        
        return boundary_index; 
        
    }
    

};