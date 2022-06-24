class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def dfs(start_index: int) -> bool:
            if start_index == len(s):
                return True
            if start_index in memo:
                return memo[start_index] 
            
            ok = False
            for word in wordDict:
                if s[start_index:].startswith(word):
                    if(dfs((start_index + len(word)))):
                        ok = True
            
            memo[start_index] = ok
            
            return memo[start_index]
        
        return dfs(0)
        