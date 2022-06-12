class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pre = []
        
        for _ in range(len(nums)):
            pre.append(1)
            
        for i in range(1, len(pre)):
            pre[i] = nums[i-1] *  pre[i-1]
        
        prev = nums[-1]
        for i in range(len(pre) -2, -1, -1):
            pre[i] *= prev
            prev *= nums[i]

        return pre
            
        
        
        
        