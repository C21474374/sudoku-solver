def solve_sudoku(board):
    def is_valid(board, row, col, num):
        # Check if the number is not repeated in the row, column, or 3x3 box
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False
        return True

    def solve(board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:  # 0 means the cell is empty
                    for num in range(1, 10):
                        if is_valid(board, row, col, num):
                            board[row][col] = num
                            if solve(board):
                                return True
                            board[row][col] = 0  # Backtrack
                    return False  # No valid number found
        return True  # Puzzle solved

    if solve(board):
        return board
    else:
        return None  # Return None if no solution exists
