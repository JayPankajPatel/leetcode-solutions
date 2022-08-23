class Solution:
    def isValid(self, s: str) -> bool:
        from collections import deque
        
        check = {
            ']':'[',
            '}': '{', 
            ')': '('
        }
        stack = deque()
        
        for x in s:
            if stack and x in check and stack[-1] == check[x]:
                stack.pop()
            else:
                stack.append(x)
            
        return len(stack) == 0
        
        
       