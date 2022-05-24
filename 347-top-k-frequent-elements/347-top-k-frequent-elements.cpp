class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        using namespace std; 
        
        unordered_map<int,int> count;
        vector<vector<int>> freq(nums.size()+1); 
        
        for(const int& x : nums){
            count[x]++;
        }
        
        for(const auto& [num,ocur] : count){
            
            freq[ocur].push_back(num);
        }
        
        vector<int>ans;
        
        for(int i = freq.size()-1; i >= 0; i--){
            for(int j = 0; j < freq[i].size(); j++){
                ans.push_back(freq[i][j]);
                if(ans.size() == k)
                    return ans;
            }
        }
        
        return {};
    }
};