class Solution {
public:
    bool isAnagram(string s, string t) {
        
        if(s.size() != t.size())
            return false;
        std::unordered_map<char,int> check;
        
        for(int i = 0; i < s.size(); i++) {
            
            check[s[i]]++;
            check[t[i]]--;
        }
        
        
        for(auto&&[key,value] : check) {
            
            if(value > 0)
                return false;
        }
        
        
        
            
        return true; 
        
    }
};