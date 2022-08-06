class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        right = 0
        left = 0
        window = set()
        max_distance = 0
        while not (right == len(s)):
            if s[right] not in window:
                window.add(s[right])
                right += 1
            elif s[right] in window:
                window.remove(s[left])
                left += 1
            max_distance = max(max_distance, right - left)
        return max_distance
                
                
        