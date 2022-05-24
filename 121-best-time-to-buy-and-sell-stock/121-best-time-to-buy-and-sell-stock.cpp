class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int max_profit = 0; 
        int min_val = pow(10,4);
        
        
        
        for(int i = 0; i < prices.size(); i++)
        {
            min_val = min(prices[i], min_val);
            max_profit = max(prices[i]-min_val, max_profit);
        }
        
        
        return max_profit; 
        
    }
};