class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        s_window, p_check = {}, {}
        res = []
        for i in range(len(p)):
            s_window[s[i]] = s_window.get(s[i], 0) + 1
            p_check[p[i]] = p_check.get(p[i], 0) + 1
        
        if s_window == p_check:
            res.append(0)
        left = 0 
        for right in range(len(p), len(s)):
            s_window[s[right]] = s_window.get(s[right], 0) + 1
            s_window[s[left]] -= 1
            
            if s_window[s[left]] <= 0:
                s_window.pop(s[left])
            left += 1    
            if s_window == p_check:
                res.append(left)
        return res