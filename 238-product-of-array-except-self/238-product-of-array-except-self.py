class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pre = []
        
        for _ in range(len(nums)):
            pre.append(1)
            
        for i in range(1, len(pre)):
            pre[i] = nums[i-1] *  pre[i-1]
        
        post = []
        
        for _ in range(len(nums)):
            post.append(1)
        
        for i in range(len(nums)-1, 0, -1):
            post[i - 1] = post[i] * nums[i]
            
        print(post)
        res = []
        
        for i, x in enumerate(pre):
            res.append(pre[i] * post[i])
            
           
        
        
        return res
            
        
        
        
        