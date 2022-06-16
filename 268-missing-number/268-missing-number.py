class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        
        expected_sum = 0
        for x in range(n + 1):
            expected_sum += x
            
        actual_sum = 0
        for _, x in enumerate(nums):
            
            actual_sum += x
        
        return expected_sum - actual_sum
            
        
        