class Solution {
public:
    int climbStairs(int n) {
        static unordered_map<int,int> memo; 
        if(memo.find(n) != memo.end()) {return memo[n];} 
        if(n < 0) return 0; 
        if(n == 0) return 1; 
                
        memo[n] = (climbStairs(n-1) + climbStairs(n-2));
        
        return memo[n]; 
        
    }
};