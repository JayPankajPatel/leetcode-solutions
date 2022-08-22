class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        
        word = list(palindrome)
        
        n = len(word)
        
        for i in range(n):
            if not(word[i] == 'a'):
                word[i] = 'a'
                break
                
        final = "".join(word) 
        
        if final < palindrome and not(final[::-1] == final):
            return final
        else:
            word = list(palindrome)
            word[-1] = 'b'
            return "".join(word)
        
        
        