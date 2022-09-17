class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        
        count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    self.helper(grid, i, j)
        
        return count
    
    def helper(self, grid: List[List[str]], row: int, col: int) -> None:
        while row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == '0':
            return
        
        grid[row][col] = '0'
        
        self.helper(grid, row + 1, col)
        self.helper(grid, row - 1, col)
        self.helper(grid, row, col + 1)
        self.helper(grid, row, col - 1)