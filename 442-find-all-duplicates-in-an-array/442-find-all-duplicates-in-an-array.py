class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        our_set = set(nums)
        res = []
        
        for _, x in enumerate(nums):
            if x in our_set:
                our_set.remove(x)
            else:
                res.append(x)
        return res
        