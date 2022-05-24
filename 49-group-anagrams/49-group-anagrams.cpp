class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        using namespace std; 
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);
        unordered_map<string,vector<string>> my_map;
        
        char char_count[27] = {};
        char_count[26] = 0;
       
        for(string & curr_str : strs) {
            std::fill_n(char_count, 26, 1);
            
            for(int j = 0; j < curr_str.size(); j++) {
                char_count[curr_str[j] - 'a']++;
                for(auto x : char_count)
                {
                    cout << x << " "; 
                }
                cout << endl;
            }

            string to_hash(char_count);
            
            my_map[to_hash].push_back(curr_str); 
        }
        
        vector<vector<string>> ans;
        
        for( auto&[key,value] : my_map) {
            ans.push_back(value);
        }
        
        return ans;
    }
};