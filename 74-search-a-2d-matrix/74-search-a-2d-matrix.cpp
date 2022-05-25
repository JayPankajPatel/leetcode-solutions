class Solution {

private:
    bool binary_search(std::vector<int>& row, int target) {
        
        int l = 0; 
        int r = row.size()-1; 
        
        while(l <= r) {
            
            int mid = (r+l)/2;
            int value = row[mid];
            if(target == value)
                return true; 
            if(target < value)
                r = mid - 1; 
            else
                l = mid + 1; 
        }
        
        return false; 
    }
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        
        int m = matrix.size();  
        bool found = false; 
        for(int i = 0; i < m; i++) {
            
           found = found || binary_search(matrix[i], target);
           if(found)
               return true; 
        }
        
        return false; 
    }
};