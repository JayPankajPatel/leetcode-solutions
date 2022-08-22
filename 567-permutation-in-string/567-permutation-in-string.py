class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        window = [0] * 26
        check = [0] * 26
        for i in range(len(s1)):
            check[ord(s1[i]) - ord('a')] += 1
            window[ord(s2[i]) - ord('a')] += 1
            
        
        l, r = 0, len(s1)-1 
        if window == check:
                return True
        while r != len(s2)-1:
            if window == check:
                return True
            window[ord(s2[l]) - ord('a')] -= 1
            l += 1
            if window == check:
                return True
            r += 1
            window[ord(s2[r]) - ord('a')] += 1
            if window == check:
                return True
            
        
        return window == check
        