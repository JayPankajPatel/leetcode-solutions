class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        NUMPAD = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        if len(digits) == 0:
            return []
        def perm(route = []): 
            if len(route) == len(digits):
                res.append("".join(route))
                return
            letters = NUMPAD[digits[len(route)]]
            for letter in letters: 
                route.append(letter)
                perm(route)
                route.pop()
                
            
        perm()
    
        return res