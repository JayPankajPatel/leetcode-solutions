class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = float('inf') *-1
        max_sum = float('inf') *-1
        
        for x in nums:
            max_so_far = max(x, max_so_far + x)
            max_sum = max(max_sum, max_so_far)
            
        return max_sum
            
            
            
            