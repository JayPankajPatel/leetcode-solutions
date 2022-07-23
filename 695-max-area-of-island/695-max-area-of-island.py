class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_so_far = 0
        num_row = len(grid)
        num_col = len(grid[0])
        def get_neighbors(coor):
            res = []
            delta_row = [0, 1, 0, -1]
            delta_col = [-1, 0, 1, 0]
            n = len(delta_row)
            row, col = coor
            for i in range(n):
                neighbor_row = row + delta_row[i]
                neighbor_col = col + delta_col[i]
                
                if 0 <= neighbor_row < num_row and 0 <= neighbor_col < num_col:
                    if grid[neighbor_row][neighbor_col] == 1:
                        res.append((neighbor_row, neighbor_col))
            return res
        
        def bfs(root):
            queue = deque([root])
            row, col = root
            grid[row][col] = 0
            count = 1
            while(len(queue)):
                node = queue.popleft()
                for neighbor in get_neighbors(node):
                    _r, _c = neighbor
                    queue.append(neighbor)
                    grid[_r][_c] = 0
                    count += 1
            return count
        
        for r in range(num_row):
            for c in range(num_col):
                if grid[r][c] == 1:
                    max_so_far = max(max_so_far, bfs((r, c)))
        return max_so_far
                    
                        