class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)
        expected_sum = 0
        for x in range(n + 1):
            expected_sum += x
        
       
        
       
        actual_sum = sum(nums)
        
        
        return expected_sum - actual_sum
            
        
        