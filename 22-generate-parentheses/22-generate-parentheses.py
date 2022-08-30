class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        
        def recurse(open_count, closed_count):
            nonlocal res 
            nonlocal stack
            if open_count == closed_count == n:
                res.append("".join(stack))
                return
            if open_count < n:
                stack.append("(")
                recurse(open_count + 1, closed_count)
                stack.pop()
                
            if closed_count < open_count:
                stack.append(")")
                recurse(open_count, closed_count + 1)
                stack.pop()
        recurse(0, 0)
        return res