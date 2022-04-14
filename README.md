# Project Title: Sudoklver

## Team Members:
- Moyosore Weke
- Testimony Adeyemi
- Petronalla 
- Topister Onyango
- Eleaanor Wepnog

## Data structure and algorithm used:
- **Data structure: Recursion and 2D arrays**
  - We used a recursive data structure because we designed the algorithm in a way that it calls itself, Recursion is the process whereby a function calls itself. We are also storing the matrix of the board, cells and values in a 2D-array

- **Algorithm: Backtracking Algorithm**
  - Backtracking is an algorithmic technique that aims to use a brute force approach to get all the solutions to a problem. It uses the recursive call to build the solution step by step and find the solution set by increasing the level over time. Essentially, you keep trying numbers in empty spots until there aren't any that are possible, then you backtrack and try different numbers in the previous slots. This is a better optimized algorithm than the naive approach where you just try every number 
  - How It works in simpler logic
      - A digit in the wrong location often quickly shows that the solution is infeasable. With n entries left, if there are no entries, n = 0, left, we are finished, indicate succes;
      - Otherwise, find a square that is not yet filled, and for each digit from 1 to 9. 
      - Place the digit in the digit in that square and see whether the the solution is feasible, and if so call backtracking algorithm recursively
      - If the algorithm indicates success, we are finished, otherwise, try the next digit; and if no digit works, there is no solution.


## Project Description:

Sudoku is a logic-based puzzle that plays with numbers from 1 to 9. The puzzle first appeared in a newspaper in France in November 1892. Most of the essays that study Sudoku solvers show different types of Sudoku solvers algorithm. Thanks to its simple rules, it's fascinating and very easy to learn. There are  many now Classic Sudoku including various kinds of Sudoku puzzles,  9X9 grid with given clues, Mini Sudoku consisting of 4X4 ​​or 6X6 size grids in different locations etc. In our project, we focused is mainly on the classic Sudoku that is, the 9X9 grid. 

To play Sudoku, the player only needs to be familiar with the numbers from 1 to 9 and be able to think logically. The goal of this game is clear: to fill and complete the grid using the numbers from 1 to 9. The challenging part lays on the restrictions imposed on the player to be able to fill the grid

The restrictions are as follows:
  - Each row must contain the numbers from 1 to 9, without repetitions
  - Each column must contain the numbers from 1 to 9, without repetitions
  - The digits can only occur once per block (nonet)
  - The sum of every single row, column and nonet must equal 45
  - Each puzzle has a unique solution

Each Sudoku puzzle begins with some cells filled in. These numbers are chosen such that there is a unique solution to the Sudoku.The Sudoklver(sudoku solver) aims to help players of sudoku's solve this puzzel in a much shorter time that they would have spent. Also most people who play the sudoku games which are at the back of the newspaper often have to wait for the results to come in the next day so therefore the solver will be there for them to easily to check their solutions early to know if there are right or wrong.

## Correctness of Algorithm
In our project Sudoklver(Sudoku Solver0, we are using the Backtracking Algorithm to develop a working solution. Here we are going to check the correctness of that Algorithm, we are going to take a closer look at the **recursion and the backtracking algorithm** which is implemented by the `solveSudoku()` function.

### solveSudoku function

```Python
def solveSudoku(sudoku, row, col):
    global count 
    count += 1
    
    if count > 1000:
        return False
    
    if row== N - 1 and col == N:
        return True

    if col == N:
        row += 1
        col = 0

    if sudoku[row][col] > 0:
        return solveSudoku(sudoku, row, col + 1) 

    for num in range(1, N + 1):
        if isValid(sudoku, row, col, num):
            sudoku[row][col] = num 
            if solveSudoku(sudoku, row, col + 1):  
                return True
       
        sudoku[row][col] = 0 
     
   
    return False  
```
From the code above, we can see that the function is correct since each time the process is called the following happens:

- First, we test out the base condition `if row== N - 1 and col == N:` to ensure that we are not at the end of the board, if we are at the end of the board then we return `True` because we can only get to the end of the board when the algorithm solves sudoku and we have found all values.

- Next, we also check if we are in the last column `  if col == N: `, and this moves to the next row to test out values, the way the algorithm is designed is we test out each value in a column and we move by column when we can assign a value(Going to come back to this)

- After that, we actually check if a value is assigned at the position we want to put it in, for instance of in our puzzle a value is in a position, we check for that and if a value is assigned them if it isn’t empty(if it is greater than 0) then we move to the next column, by recursively calling solve sudoku. 

- And if our if statement is wrong( `if sudoku[row][col] > 0`), then we start testing  for each number from 1 to 10 which is that `for loop` there. So as we can see the for loop is correct because we first test if it is safe to assign a number, by calling the isvalid function and putting in the number we are testing, if it is safe we assign the number to that position and we move to the next column, 

- If it is not safe to assign a value in a position then we backtrack `sudoku[row][col] = 0 ` to the previous position the previous value we assigned and try other numbers this helps to save time 


