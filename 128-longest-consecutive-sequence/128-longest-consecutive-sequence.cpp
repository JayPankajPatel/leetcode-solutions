class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        
        int seq_count {0}; 
        int max_seq_count {0}; 
        std::unordered_set<int> seq(nums.begin(), nums.end()); 
        
        for(auto&& x : seq)
        {
            if(seq.find(x-1) == seq.end())
            {
                seq_count++; 
                
                while(seq.find(x+seq_count) != seq.end())
                {
                    ++seq_count;
                }
                
                
            }
            
            max_seq_count = max(seq_count, max_seq_count);
            
            seq_count = 0; 
        }
        
        
        return max_seq_count;
        
        
        
    }
};