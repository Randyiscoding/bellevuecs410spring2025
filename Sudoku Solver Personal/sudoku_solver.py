def solve_sudoku(board):
    '''Not that you asked but this is how i wouldve solved a given sudoku. Essential figure out all the possibilities
    that might fit into a given position and then fill in each block with that value. After some googling in the process
    I learned this was called the "Minimum Remaining Value" heuristic which was pretty cool and works similar to the
    brute force version though this is supposed to be faster (I'm not sure the O(n) time but i imagine since its not
    trying every number it is somewhat faster)  '''
    b=board
    possibilities = {}
    digits = set(range(1, 10))

    for row in range(len(b)):
        for col in range(len(b[row])):
            if b[row][col] == 0:
                # Get values from row
                row_vals = set(b[row])

                # Get values from column
                col_vals = {b[r][col] for r in range(len(b))}

                # Get values from 3x3 square
                box_row = (row // 3) * 3
                box_col = (col // 3) * 3
                box_vals = {b[r][c] for r in range(box_row, box_row + 3)
                            for c in range(box_col, box_col + 3)}

                # Combine all values to exclude
                used_vals = row_vals | col_vals | box_vals
                used_vals.discard(0)  # Remove 0 since it's just the empty placeholder

                # Store the remaining possibilities
                possibilities[(row, col)] = digits - used_vals

    if not possibilities:
        return True
    else:
        cord = min(possibilities, key= lambda k: possibilities[k])
        for elements in possibilities[cord]:
            row,col = cord
            b[row][col] = elements
            if solve_sudoku(b):
                return True
            b[row][col] = 0
        return False
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
