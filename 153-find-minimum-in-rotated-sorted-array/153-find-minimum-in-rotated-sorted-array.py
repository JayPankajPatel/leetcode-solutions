class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        boundary_index = -1
        left, right = 0, len(nums) -1
        
        while(left <= right):
            mid = (left + right) // 2
            
            if nums[mid] < nums[-1]:
                right = mid - 1
                boundary_index = mid
            else:
                left = mid + 1
        
        return nums[boundary_index]