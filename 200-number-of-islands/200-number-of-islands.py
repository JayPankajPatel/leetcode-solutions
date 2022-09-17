class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])
        def get_neighbors(coor):
            nonlocal num_cols
            nonlocal num_rows
            row, col = coor
            delta_row = [0, 1, 0, -1]
            delta_col = [-1, 0, 1, 0]
            res = []
            for i in range(len(delta_row)):
                neigh_row = row + delta_row[i]
                neigh_col = col + delta_col[i]
                
                if 0 <= neigh_row < num_rows and 0 <= neigh_col < num_cols:
                    if grid[neigh_row][neigh_col] == '1':
                        res.append([neigh_row, neigh_col])
            return res
        
        def bfs(start):
            from collections import deque
            queue = deque([start])
            
            while queue:
                node = queue.popleft()
                for row, col in get_neighbors(node):
                    if grid[row][col] == '1':
                        grid[row][col] = '0'
                    queue.append([row, col])
            
        
        counter = 0
        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == '1':
                    bfs([i, j])
                    counter += 1
        return counter
                
        