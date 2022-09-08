# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        my_map = set()
        i = 0
        while head and head.next:
            if head in my_map:
                return head
            my_map.add(head)
            head = head.next
            i += 1
        
        return None
                
        
        