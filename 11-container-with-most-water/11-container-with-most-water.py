class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        
        
        l, r = 0, len(height) - 1
        
        while (l < r):
            distance = abs(l - r)
            area = distance * min(height[l], height[r])
            max_area = max(area, max_area)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        
        return max_area
                