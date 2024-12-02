def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    box_start_row, box_start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(box_start_row, box_start_row + 3):
        for j in range(box_start_col, box_start_col + 3):
            if board[i][j] == num:
                return False
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return board
                        board[row][col] = 0
                return False
    return board

def sudoku_solver(input_board):
    if not isinstance(input_board, list) or len(input_board) != 9 or any(len(row) != 9 for row in input_board):
        raise ValueError("Invalid board format.")
    result = solve_sudoku(input_board)
    return result if result else None
