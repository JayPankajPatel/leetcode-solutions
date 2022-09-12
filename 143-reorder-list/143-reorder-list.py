# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # find the middle of the list
        
        slow, fast = head, head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
    
        cur = slow.next
        prev = slow.next = None
        
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        start, end = head, prev
        
        while end:
            tmp1, tmp2 = start.next, end.next
            start.next = end
            end.next = tmp1
            start = tmp1
            end = tmp2
        
       
        
        
        
           
        
        