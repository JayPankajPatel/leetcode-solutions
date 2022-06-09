class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        
        std::vector<int> merge{nums1};
        
        for(auto&& x : nums2)
            merge.push_back(x); 
        
        std::sort(merge.begin(), merge.end()); 
        
        if(merge.size() % 2 != 0) {
            
            int mid = merge.size()/2; 
            
            return merge[mid]; 
        }
        
        else {
            
            int mid = merge.size() / 2 - 1;
            
            return (double)(merge[mid] + merge[mid +1]) / 2;
            
            
        }
        
        
        return 0.0; 
    }
};