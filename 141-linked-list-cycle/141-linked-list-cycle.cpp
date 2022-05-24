/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        
        ListNode *slow = new ListNode();
        ListNode *fast = new ListNode();
        
        slow -> next = head; 
        fast -> next = head;
        
        while(fast -> next && fast -> next -> next)
        {
            if(slow == fast){return true;}
            else
            {
                fast = fast -> next -> next;
                slow = slow -> next; 
            }
        }
        
        
        return false; 
        
    }
};