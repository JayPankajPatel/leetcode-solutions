class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not(len(s) == len(t)):
            return False
        
        check_s = {}
        check_t = {}
        
        for x in s:
            check_s[x] = check_s.get(x,0)+1
        for y in t:
            check_t[y] = check_t.get(y,0)+1
            
        return check_s == check_t