from NumberClass import SingleNumber
from SudokuPrint import print_sudoku

solved_numbers=0

sudoku_grid = [
    [None,None,3,None,None,9,None,8,None],
    [7,4,None,5,3,None,None,None,9],
    [None,None,9,None,6,None,None,None,4],
    [8,1,7,3,4,None,9,2,None],
    [None,9,4,7,2,6,None,None,1],
    [2,6,None,8,None,None,4,None,None],
    [None,7,None,None,1,None,None,None,None],
    [9,5,1,None,None,None,None,None,2],
    [6,None,None,None,None,None,1,9,7],
]

# sudoku_grid2=[[4,None,7,None,6,8,None,3,None],
# [9,None,None,3,None,2,None,None,None],
# [None,None,None,1,None,7,2,4,None],
# [1,None,2,6,8,None,4,9,None],
# [5,None,8,None,None,4,None,2,None],
# [None,6,None,None,None,None,None,8,None],
# [8,7,None,None,None,6,3,None,4],
# [3,None,None,8,None,1,7,6,2],
# [None,None,6,None,None,None,None,1,9]]


#  Iterates through the grid and replaces the numbers with Single Number Objects
for i, row in enumerate(sudoku_grid):
    for j, cell in enumerate(row):
        sudoku_grid[i][j]=SingleNumber(i,j,sudoku_grid[i][j])

# Generates the Object Lists for 3X3 Squares:
GridX0Y0 = [x for x in sum(sudoku_grid, []) if x.GridLocation == 'X0Y0']
GridX0Y1 = [x for x in sum(sudoku_grid, []) if x.GridLocation == 'X0Y1']
GridX0Y2 = [x for x in sum(sudoku_grid, []) if x.GridLocation == 'X0Y2']

GridX1Y0 = [x for x in sum(sudoku_grid, []) if x.GridLocation == 'X1Y0']
GridX1Y1 = [x for x in sum(sudoku_grid, []) if x.GridLocation == 'X1Y1']
GridX1Y2 = [x for x in sum(sudoku_grid, []) if x.GridLocation == 'X1Y2']

GridX2Y0 = [x for x in sum(sudoku_grid, []) if x.GridLocation == 'X2Y0']
GridX2Y1 = [x for x in sum(sudoku_grid, []) if x.GridLocation == 'X2Y1']
GridX2Y2 = [x for x in sum(sudoku_grid, []) if x.GridLocation == 'X2Y2']


# Now Iterate through each Object in the grid:
def ScanGrid():
    global solved_numbers
    solved_numbers=0

    for row_index,row in enumerate(sudoku_grid):
        for number_index,number in enumerate(row):
            if number.Solved==True:
                solved_numbers+=1 
            if number.Solved==False:
            # Delete potential numbers based on others in same Vertical Line            
                Other_numbers_in_X_line=[0,1,2,3,4,5,6,7,8]
                Other_numbers_in_X_line.remove(number_index)
                for other_X_number in Other_numbers_in_X_line:
                    number.RemovePossibleNumber(sudoku_grid[row_index][other_X_number].Number)
            # Delete potential numbers based on others in same Horizontal Line     
                Other_numbers_in_Y_line=[0,1,2,3,4,5,6,7,8]
                Other_numbers_in_Y_line.remove(row_index)
                for other_Y_number in Other_numbers_in_Y_line:
                    number.RemovePossibleNumber(sudoku_grid[other_Y_number][number_index].Number)
            # Delete potential numbers based on others in same Grid 
                current_grid_list = globals()[f"Grid{number.GridLocation}"]
                for grid_other_number in current_grid_list:
                    number.RemovePossibleNumber(grid_other_number.Number)

def TakeGridInput():
    print ("Enter your Grid as one long number with '-' for unknown numbers:")
    grid_string = input('Sudoku:')
    sudoku_grid_is_valid = len(grid_string) == 81 and all(char.isdigit() or char == '-' for char in grid_string)
    if sudoku_grid_is_valid ==False:
        print ('Invalid Grid - Please Try Again')
        TakeGridInput()
    else:
        formatted_grid_list = [grid_string[i:i+9] for i in range(0, len(grid_string), 9)]
        return formatted_grid_list

def solve_puzzle():
    ScansNeeded=0
    while solved_numbers != 81:
        ScansNeeded+=1
        ScanGrid()
    print (f'Finished! in {ScansNeeded} passes of the puzzle')
    print_sudoku(sudoku_grid)
    



solve_puzzle()