class Solution:
    def isPalindrome(self, check: str) -> bool:
        l, r = 0, len(check)-1
        while l < r:
            if not(check[l] == check[r]):
                return False
            l += 1
            r -= 1
        return True
    
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        
        word = list(palindrome)
        
        n = len(word)
        
        for i in range(n):
            if not(word[i] == 'a'):
                word[i] = 'a'
                break
                
        
        if "".join(word) < palindrome and not(self.isPalindrome("".join(word))):
            return "".join(word)
        else:
            word = list(palindrome)
            word[-1] = 'b'
            return "".join(word)
        
        
        