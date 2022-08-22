class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        window = defaultdict(int)
        check = defaultdict(int) 
        
        for x in t:
            check[x] += 1
        
        have, need = 0, len(check)
        
        l = 0
        min_distance = float('inf')
        ptrs = [-1, -1]
        
        for r in range(len(s)):
            window[s[r]] += 1
            
            if s[r] in check and window[s[r]] == check[s[r]]:
                have += 1
            
            while have == need:
                if min_distance > (r - l + 1):
                    min_distance = r - l + 1
                    ptrs = [l, r]
                
                window[s[l]] -= 1
                if s[l] in check and window[s[l]] < check[s[l]]:
                    have -= 1
                l += 1
        return s[ptrs[0]: ptrs[1]+1]