class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minb, maxs = float("inf"), -1
        max_profit = 0
        
        for x in prices:
            minb = min(minb, x)
            max_profit = max((x-minb), max_profit)
            
        return max_profit
        