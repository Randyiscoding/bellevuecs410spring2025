def is_valid(board, row, col, num):
    """
    Determine if it's valid to place 'num' at position (row, col) on the Sudoku board.
    Implement the necessary checks.
    """
    b = board
    r = row
    c = col
    n = num
    if n in b[r]:
        return False
    for x in range(len(b)):
        if b[x][c] == n:
            return False
    for x in range(r, r + 3):
        for y in range(r, r + 3):
            if b[x][y] == n:
                return False
    return True
    pass

def solve_sudoku(board):
    """
    Solve the provided Sudoku board using backtracking.
    Fill in the solution directly into the board.
    Return True if a solution exists, otherwise return False.
    """
    for row in range(len(b)):
        for cell in range(len(b[row])):
            if b[row][cell] == 0:
                for num in range(1,10):
                    if is_valid(b,row,cell,num) == True:
                        b[row][cell] = num
                        if sudo(b):
                            return True
                        else:
                            b[row][cell] = 0
                return False
    return True
    pass

if __name__ == "__main__":
    import sys

    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python sudoku_solver.py <input_file>")
        sys.exit(1)

    # Read Sudoku board from the input file
    input_file = sys.argv[1]
    with open(input_file, "r") as file:
        sudoku_board = [[int(num) for num in line.split()] for line in file.readlines()]

    print("Input Sudoku Board:")
    for row in sudoku_board:
        print(" ".join(map(str, row)))

    # Solve the Sudoku board
    if solve_sudoku(sudoku_board):
        print("\nSolved Sudoku Board:")
        for row in sudoku_board:
            print(" ".join(map(str, row)))
    else:
        print("\nNo solution exists.")
