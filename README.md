# Sudoku Solver

This Python program provides a simple Sudoku solver that utilizes logic to deduce possible numbers for each cell without resorting to brute force

## Features

- Solves Sudoku puzzles by analyzing the logical possibilities of each cell.
- User-friendly interface prompting input from the user in the command line interface.
- Objects are used to represent each cell, containing possible numbers and solved status.

## Usage

1. Run the program in the command line.
2. Follow the prompts to input the Sudoku puzzle as a string of numbers with gaps for unknown cells.
3. The program will attempt to solve the puzzle and return the completed Sudoku grid.

## How it Works

The Python Sudoku solver operates by a series of logical steps to deduce the correct numbers for each cell in the Sudoku grid:

1. **User Input**: The user is prompted to input the Sudoku puzzle as a long string of numbers, with gaps representing unknown cells. This input is then converted into a series of cell objects, each initialized with its possible numbers and a solved status.

2. **Grouping and Initialization**: The program begins by creating a list of relevant groups, which correspond to the large 3x3 grids within the Sudoku puzzle.

3. **Logic-Based Solving**: The solver iterates through each cell in the Sudoku grid. For each unsolved cell, it first scans the same vertical line and removes numbers that have already been solved within that column. It then performs a similar operation for the horizontal line and the 3x3 grid, removing all possible numbers.

4. **Single Possibility Check**: If, after applying the above steps, there is only one possible number remaining for a cell, the solver fills in that cell with the remaining number and marks it as solved.

5. **Iterative Process**: The solver repeats the above steps for each cell in the Sudoku grid. It continues to iterate and make deductions until either the puzzle is completely solved or no further progress can be made.

This logical deduction approach allows the solver to efficiently solve Sudoku puzzles without resorting to exhaustive search algorithms. However, it does have limitations, particularly with highly complex puzzles where logical deductions alone may not suffice to make progress.

## Limitations

- Due to the reliance on completed cells to progress rather than inferred options, there is a limitation on the difficulty of puzzles this solver can handle.
- Difficulty limitation can be addressed by implementing a [backtracking algorithm](https://en.wikipedia.org/wiki/Backtracking) to handle more complex puzzles, working instead with a brute force approach and using the current process as a validity checker rather than a complete solver



