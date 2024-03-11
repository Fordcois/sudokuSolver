from NumberClass import SingleNumber
from SudokuPrint import print_sudoku

Pattern = [
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



sudoku_grid2=[[4,None,7,None,6,8,None,3,None],
[9,None,None,3,None,2,None,None,None],
[None,None,None,1,None,7,2,4,None],
[1,None,2,6,8,None,4,9,None],
[5,None,8,None,None,4,None,2,None],
[None,6,None,None,None,None,None,8,None],
[8,7,None,None,None,6,3,None,4],
[3,None,None,8,None,1,7,6,2],
[None,None,6,None,None,None,None,1,9]]




def solve_puzzle(sudoku_grid):
    
    grid = [[None] * 9 for _ in range(9)]


    for i, row in enumerate(sudoku_grid):
        for j, cell in enumerate(row):
            grid[i][j]=SingleNumber(i,j,sudoku_grid[i][j])
    
    solved_numbers=0
    scans_complete=0

    # Generates the Object Lists for 3X3 Squares:
    grids = {}
    for x in range(3):
        for y in range(3):
            grid_name = f"X{x}Y{y}"
            grids[grid_name] = [x for x in sum(grid, []) if x.GridLocation == grid_name]

        

    while solved_numbers !=81 and scans_complete!=729:
        
        solved_numbers=0
        scans_complete+=1
        
        for row_index,row in enumerate(grid):
            for number_index,number in enumerate(row):
                if number.Solved==True:
                    print (f'{number} is {number.Solved}')
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
        print (f'Puzzle Solved! after {scans_complete}')
    if scans_complete == 729:
        print ('Unable to Solve Puzzle...')
    
    print_sudoku (grid)


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
                    line_being_constructed.append(int(char))
                else:
                    line_being_constructed.append(None)
            Built_Grid.append(line_being_constructed)
        solve_puzzle(Built_Grid)



MegaString= '-5-----76--673--2-----8------526--3-4-----9-------1----9-17-3----7--8--------5-1-'
TestString='111111111*2222222233333333*444444444555555555666666666777777777888888888999999999'
PatternString='--3--9-8-74-53---9--9-6---481734-92--94726--116-8--4---7--1----951-----26-----197'

TakeGridInput()

print (Pattern[0])