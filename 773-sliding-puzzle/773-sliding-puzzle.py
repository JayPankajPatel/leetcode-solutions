class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        valid_idx_swap = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }
        num_row = 2
        num_col = 3
        def serialize(board: List[List[int]]) -> str:
            ser_list = ""
            for i in range(num_row):
                for j in range(num_col):
                    ser_list += str(board[i][j])
            return ser_list
        
        def get_puzzles(puzzle: str) -> List[str]:
            idx_zero = -1 
            lst_puzzle = list(puzzle)
            for i, x in enumerate(lst_puzzle):
                if x == "0":
                    idx_zero = i
                    break
            res = []
            for i in valid_idx_swap[idx_zero]:
                dpcpy_lst_puzzle = lst_puzzle[:]
                temp = dpcpy_lst_puzzle[i]
                dpcpy_lst_puzzle[i] = dpcpy_lst_puzzle[idx_zero]
                dpcpy_lst_puzzle[idx_zero] = temp
                res.append("".join(dpcpy_lst_puzzle))
            return res
        def bfs():
            queue = deque()
            ser_board = serialize(board)
            queue.append([ser_board, 0])
            visited = set()
            visited.add(ser_board)
            while queue:
                for _ in range(len(queue)):
                    pos_sol, steps = queue.popleft()
                    for puzzle in get_puzzles(pos_sol):
                        if pos_sol == "123450":
                            return steps 
                        if puzzle not in visited:
                            queue.append([puzzle, steps + 1])
                            visited.add(puzzle)
            return -1
        return bfs()
                    
            
        