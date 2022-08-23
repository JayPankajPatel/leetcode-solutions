/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    bool isPalindrome(ListNode* head) {
        
        ListNode* slow = head;
        ListNode* fast = head;
        ListNode* dummy = head; 
        
        while(fast && fast -> next)
        {
            fast = fast ->next->next;
            slow = slow -> next; 
        }
        
        ListNode* prev = NULL; 
        ListNode* temp = new ListNode(); 
        while(slow)
        {
            temp = slow -> next;
            slow -> next = prev;
            prev = slow;
            slow = temp; 
            
        }
        
        while(prev)
        {
            if(prev -> val != dummy-> val){return false;}
            else
            {
                prev = prev -> next; 
                dummy = dummy -> next; 
            }
        }
        
        delete temp, dummy; 
        
        return true; 
    }
};