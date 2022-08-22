class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False
        return math.log(n) / math.log(4) % 1 == 0
        