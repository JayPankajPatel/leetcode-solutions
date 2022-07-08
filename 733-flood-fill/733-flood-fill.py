class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        num_rows = len(image)
        num_cols = len(image[0])
        replace = image[sr][sc]
        
        def get_neighbors(coor):
            res = []
            r = coor[0]
            c = coor[1]
            delta_row = [1, 0, -1, 0]
            delta_col = [0, 1, 0, -1]
            
            n = len(delta_row)
            
            for i in range(n):
                neigh_row = r + delta_row[i]
                neigh_col = c + delta_col[i]
                
                if 0 <= neigh_row and neigh_row < num_rows and 0 <= neigh_col and neigh_col < num_cols:
                    if image[neigh_row][neigh_col] == replace:
                        res.append((neigh_row, neigh_col))
            return res
        
        def bfs(root):
            queue = deque([root])
            visited = [[False for c in range(num_cols)]for r in range(num_rows)]
            image[sr][sc] = color
            visited[sr][sc] = True
            
            while(len(queue)):
                node = queue.popleft()
                r, c = node
                for neighbor in get_neighbors((r, c)):
                    r, c = neighbor
                    if visited[r][c]:
                        continue
                    image[r][c] = color
                    visited[r][c] = True
                    queue.append((r, c))
        
        
        bfs((sr, sc))
        return image
            
        