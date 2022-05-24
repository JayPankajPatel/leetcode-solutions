class Solution {
public:
    bool valid(std::vector<int>& piles, int k, int h) {
        
        int sum {0};
        
        for(const double& x : piles) {
            sum += ceil((double)x/k);  
        }
        
        return sum <= h; 
    }
    int minEatingSpeed(vector<int>& piles, int h) {
        int l {1};
        int r = *std::max_element(piles.begin(), piles.end());
        int boundary_val {-1};
        
        
        while(l <= r) {
            
            int mid {(r + l)/2};
            
            if(valid(piles, mid, h)) {
                
                boundary_val = mid; 
                r = mid - 1;
            }
            
            else
                l = mid + 1; 
        }
        
        return boundary_val; 
    }
};