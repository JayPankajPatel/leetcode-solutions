class Solution:
    def romanToInt(self, s: str) -> int:
        convert = {
            "I" : 1, 
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }
        
        l = 0
        r = 1
        ans =  0
        for _ in range(len(s)):
            if r < len(s) and s[l:r+1] in convert:
                print([s[l:r+1]])
                ans += convert[s[l:r+1]]
                r += 2
                l += 2
                
            else:
                if l < len(s):
                    ans += convert[s[l]]
                r += 1
                l += 1
            
        return ans
            
            
        
        