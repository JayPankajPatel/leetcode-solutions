class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def is_palindrome(word: str) -> bool:
            return word == word[::-1]
        
        def dfs(start: int, route: List[str]) -> None:
            if start == len(s):
                res.append(route[:])
                return
            
            for i in range(start, len(s)):
                substring = s[start : i + 1]
                if is_palindrome(substring):
                    route.append(substring)
                    dfs(i + 1, route)
                    route.pop()
            return
        
        dfs(0, [])
        
        return res
        