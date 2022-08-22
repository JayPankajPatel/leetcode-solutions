class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        word = palindrome
        if len(word) == 1:
            return ""
        left, right = 0, len(word) - 1
        res = [char for char in palindrome]
        print(res)
        while left < right:
                if word[left] > 'a':
                    res[left] = 'a'
                    return ''.join(res)
                left += 1
                right -= 1
        res[-1] = 'b'
        return ''.join(res)