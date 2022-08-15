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
        n = len(s)
        
        while l < n: 
            if r < n and s[l:r+1] in convert:
                ans += convert[s[l:r+1]]
                l += 2
                r += 2
            else:
                ans += convert[s[l]]
                l += 1
                r += 1
        return ans
            
            
        
        