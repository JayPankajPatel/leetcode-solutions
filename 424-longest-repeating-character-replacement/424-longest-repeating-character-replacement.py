class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = [0] * 26
        l, r, res = 0, 0, 0
        list_s = list(s)
        
        while r != len(list_s):
            char_count[(ord(list_s[r]) - ord('A'))] += 1
            r += 1
            
            while not(sum(char_count) - max(char_count) <= k):
                char_count[(ord(list_s[l]) - ord('A'))] -= 1
                l += 1
                
            res = max(res, sum(char_count))
        return res
            
        
        
        
        