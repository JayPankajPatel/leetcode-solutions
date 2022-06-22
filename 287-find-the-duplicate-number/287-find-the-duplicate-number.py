class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        our_set = set(nums)
        
        for _, x in enumerate(nums):
            
            if x in our_set:
                our_set.remove(x)
            else:
                return x
        
        
        return x
        
        
            
            
        