class Solution {
public:
    int peakIndexInMountainArray(vector<int>& arr) {
          int l {0};
    int r {static_cast<int>(arr.size()) -2};
    int boundary_index {-1};
    
    while(l <= r)
    {
        int mid {(l+r)/2};
        
        if(arr[mid + 1] < arr[mid])
        {
            boundary_index = mid;
            r = mid - 1;
        }
        else
            l = mid + 1; 
    }
    
    
    
    return boundary_index;
    }
};