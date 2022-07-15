class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_row = len(grid)
        num_col = len(grid[0])
        def get_neighbors(coor):
            row, col = coor
            res = []
            delta_row = [0, 1, 0, -1]
            delta_col = [-1, 0, 1, 0] 
            n = len(delta_row)
            for i in range(n):
                neighbor_row = row + delta_row[i]
                neighbor_col = col + delta_col[i]
                if 0 <= neighbor_row < num_row and 0 <= neighbor_col < num_col:
                    res.append((neighbor_row, neighbor_col))
            return res
        def bfs(root):
            queue = deque([root])
            while(len(queue)):
                    node = queue.popleft()
                    for neighbor in get_neighbors(node):
                        row, col = neighbor
                        if grid[row][col] == "0":
                            continue
                        queue.append(neighbor)
                        grid[row][col] = "0"
        count = 0
        for _r in range(num_row):
            for _c in range(num_col):
                if grid[_r][_c] == "0":
                    continue
                else:
                    bfs((_r,_c))
                    count += 1
        return count
        