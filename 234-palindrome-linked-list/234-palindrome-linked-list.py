# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        res = [] * 1*10**5
        
        while head:
            res.append(head.val)
            head = head.next
            
    
        return res[::-1] == res
        