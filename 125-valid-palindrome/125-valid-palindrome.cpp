class Solution {
public:
    bool isPalindrome(string s) {
        
        int l {0};
        int r = s.size(); 
        
        while(l < r) {
            
            if(!std::isalnum(s[l])) {
                
                l++; 
            }
            else if(!std::isalnum(s[r])) {
                r--; 
            }
            
            else if(std::toupper(s[l]) != std::toupper(s[r])) {
                
                return false; 
            }
            
            else{
                l++;
                r--; 
            }
        }
        
        
        return true; 
        

        
    }
};