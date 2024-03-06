def print_sudoku(grid):
    horizontal_line = "+-------+-------+-------+"
    print(horizontal_line)
    for i, row in enumerate(grid):
        if i % 3 == 0 and i != 0:
            print(horizontal_line)
        for j, cell in enumerate(row):
            if j % 3 == 0:
                print("|", end=" ")
            print(str(cell) if cell is not None else '-', end=" ")
            if j == 8:
                print("|")
    print(horizontal_line)