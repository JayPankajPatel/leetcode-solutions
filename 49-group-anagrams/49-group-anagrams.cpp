class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        using namespace std; 
        
        unordered_map<string,vector<string>> my_map;
        
        for(int i = 0; i < strs.size(); i++)
        {
            string s = strs[i];
            sort(strs[i].begin(), strs[i].end());
            my_map[strs[i]].push_back(s); 
        }
        
        vector<vector<string>> ans;
        
        for( auto&[key,value] : my_map)
        {
            ans.push_back(value);
        }
        
    
    
        
        return ans;
    }
};