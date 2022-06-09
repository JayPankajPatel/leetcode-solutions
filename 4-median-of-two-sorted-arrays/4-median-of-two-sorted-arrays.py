class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        merge = nums1 + nums2
        
        merge.sort()
        print(merge)
        if(len(merge) % 2 != 0):
            mid = len(merge) // 2
            return merge[mid]
        else:
            
            mid = len(merge) // 2 -1 
            print((merge[mid] + merge[mid + 1]))
            return (merge[mid] + merge[mid + 1]) / 2  
        
        
 