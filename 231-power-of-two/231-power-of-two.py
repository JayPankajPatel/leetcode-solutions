class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        itr = list(bin(n))
        count = 0
        for i in range(2, len(itr)):
            if itr[i] == '1':
                count += 1
        
        return count == 1
        
        
        