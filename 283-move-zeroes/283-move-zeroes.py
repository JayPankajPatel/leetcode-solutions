class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                continue
            elif not(nums[i] == 0) and nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
            else:
                j += 1
        