class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for r in tokens:
            
            if not(r == '*' or r == '+' or r == '-' or r == '/'):
                stack.append(int(r))
            else:
                x, y = int(stack.pop()), int(stack.pop()) 
                if r == '*':
                    stack.append(y*x)
                elif r == '+':
                    stack.append(y+x)
                elif r == '-':
                    stack.append(y-x)
                elif r == '/':
                    stack.append(int(y/x))
        
        return stack[-1]