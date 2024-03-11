from NumberClass import SingleNumber
from SudokuPrint import print_sudoku

def solve_puzzle(sudoku_grid):
    grid = sudoku_grid
    solved_numbers=0
    scans_complete=0

    # Generates the Object Lists for 3X3 Squares:
    grids = {}
    for x in range(3):
        for y in range(3):
            grid_name = f"X{x}Y{y}"
            grids[grid_name] = [x for x in sum(grid, []) if x.GridLocation == grid_name]
    
    # Keep Scanning until the puzzle is solved or we've reached a maximum level of attempts
    while solved_numbers !=81 and scans_complete!=729:
        
        solved_numbers=0
        scans_complete+=1
        
        for row_index,row in enumerate(grid):
            for number_index,number in enumerate(row):
                if number.Solved==True:
                    solved_numbers+=1 
                if number.Solved==False:
                # Delete potential numbers based on others in same Vertical Line            
                    Other_numbers_in_X_line=[0,1,2,3,4,5,6,7,8]
                    Other_numbers_in_X_line.remove(number_index)
                    for other_X_number in Other_numbers_in_X_line:
                        number.RemovePossibleNumber(grid[row_index][other_X_number].Number)
                # Delete potential numbers based on others in same Horizontal Line     
                    Other_numbers_in_Y_line=[0,1,2,3,4,5,6,7,8]
                    Other_numbers_in_Y_line.remove(row_index)
                    for other_Y_number in Other_numbers_in_Y_line:
                        number.RemovePossibleNumber(grid[other_Y_number][number_index].Number)
                # Delete potential numbers based on others in same Grid 
                    current_grid_list = grids[number.GridLocation]
                    for grid_other_number in current_grid_list:
                        number.RemovePossibleNumber(grid_other_number.Number)
    if solved_numbers == 81:
        print (f'Puzzle Solved!')
    if scans_complete == 729:
        print ('Unable to Solve Puzzle...')
    
    print_sudoku (grid)

# Takes an input and generates a list of lists featuring number objects or None
def TakeGridInput():
    print ("Enter your Grid as one long number with '-' for unknown numbers:")
    grid_string = input('Sudoku:')
    sudoku_grid_is_valid = len(grid_string) == 81 and all(char.isdigit() or char == '-' for char in grid_string)
    if sudoku_grid_is_valid ==False:
        print ('Invalid Grid - Please Try Again')
        TakeGridInput()
    else:
        Built_Grid = []
        for x in range(9):
            line_being_constructed=[]
            start = x * 9
            end = start + 9
            for y,char in enumerate(grid_string[start:end]):
                if char.isnumeric():
                    value=int(char)
                else: 
                    value=None
                line_being_constructed.append(SingleNumber(y,x,value))
            Built_Grid.append(line_being_constructed)
        solve_puzzle(Built_Grid)

Example_Pattern = [
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



TakeGridInput()
