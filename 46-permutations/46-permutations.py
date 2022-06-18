class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(subset, used, res):
            if len(subset) == len(nums):
                res.append(subset[:])
                return

            for i, letter in enumerate(nums):
                # skip used letters
                if used[i]:
                    continue
                # add letter to permutation, mark letter as used
                subset.append(letter)
                used[i] = True
                dfs(subset, used, res)
                # remove letter from permutation, mark letter as unused
                subset.pop()
                used[i] = False

        res = []
        dfs([], [False] * len(nums), res)
        return res
