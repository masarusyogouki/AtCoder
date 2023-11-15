def check_row(row):
    for num in range(1, 10):
        if num not in row:
            return False
    return True

def check_column(column):
    for num in range(1, 10):
        if num not in column:
            return False
    return True

def check_subgrid(subgrid):
    for num in range(1, 10):
        if num not in subgrid:
            return False
    return True

def is_valid_sudoku(sudoku):
    # Check rows
    for row in sudoku:
        if not check_row(row):
            return False

    # Check columns
    for col in range(9):
        column = [sudoku[row][col] for row in range(9)]
        if not check_column(column):
            return False

    # Check subgrids
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid = [
                sudoku[i + ii][j + jj]
                for ii in range(3)
                for jj in range(3)
            ]
            if not check_subgrid(subgrid):
                return False

    return True

def main():
    # Read the Sudoku puzzle from input
    sudoku = []
    for _ in range(9):
        row = [int(x) for x in input().split()]
        sudoku.append(row)

    # Check if the Sudoku puzzle is valid
    if is_valid_sudoku(sudoku):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
