# Project Title: Sudoku solver

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

## Solution

The objective of our Sudoku puzzle project is that the user fills in every row/column slot with values between 1-9. As a result of the objective fulfillment the Sudoku puzzle game increases the critical thinking capability of the user, enhances human brain health, improves logical thinking, helps develop problem solving skills and uses of clues which describes how difficult the game is. For instance, 17-clue puzzles are more difficult than 30-clue puzzles. In such a way that the user simply tries filling each blank square with the numbers from 1 to 9 until a valid solution is found.

### Beneficiaries of the App 
Our app is user-friendly to everyone who wants to play Sudoku puzzles and it is not restricted to anyone. 
- **Kids**: Sudoku is a puzzle with simple, easy to understand rules that any kid can try. The need to engage in logical thinking to fill the grid correctly plus the process of trial and error they must apply will naturally and unconsciously help to develop their problem-solving skills.

    Furthermore, the challenge of solving what to a kid will seem like an easy and boring game also helps them to engage more intensely to finish it quickly and improves their concentration skills.

    These benefits of Sudoku can also help them in other areas and even improve their school performance.

- **Adults|Youths** : The first time you play an easy Sudoku level, you might find yourself noting down all the candidates for one single cell in order to keep track of your progress. The more challenges you face, the quicker you will drop these notes as your brain will retain the information naturally.

    In harder levels, notes will become essential once again, but your memory skills will still be stimulated in different ways. You will become able to remember more complicated strategies and how to apply them without referring to a tutorial. Patterns from previous games will also be memorized and you will find yourself looking for the opportunity to apply them once again.This would help improve the memory of adults 

### The solution steps includes:

- The user has to make a list of all the empty slots.

- Then select a slot and place a number between 1 and 9, in it and validate the subgrids, that is, the horizontal row, vertical column and the 3 by 3 grid associated with that slot.

- If any of the constraints fail, that is:

    - Cell constraint: each cell can only be filled with one number.

    - Row constraint: a number may only occur once in each row.

    - Column constraint: a number may only occur once in each column.

    - Box constraint: a number may occur only once in each box.

    - Leave that solution by backtracking to the previous state and repeat the second step with the next number. Otherwise, check if the goal is achieved.

- If a solution is found, stop searching and it reports success. Otherwise repeat step 2 to 4 recursively.


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

## Efficiency of the Algorithm

In this section, we will be analysing the efficiency of the algorithm we used while implementing our project: The Backtracking Algorithm and the choice of Data Structure which is Recursion.

### Time Complexity: 
The time complexity applied in this algorithm is `O (n ^ m) `where the range of possibilities for each grid (that is, 9 in the algorithm) is n, whereas the number of blank spaces is m. Designing a grid size of N*N where N is 9, a perfect square, the recurrence equation is denoted as:
                                  T(M) = 9*T(M-1) + O (1)                         { for N, when M = N*N and T(N) is the running time of the solution}
 Solving the recurrence by the backtracking algorithm from a single blank slot yields O(9^M). 
 
 The logic behind this is that If there is only a single unoccupied slot, the program has n number of options to consider, and it must, in the worst-case scenario, exhaust them all. If there are two empty spots, the program must consider n different options for the first spot and n different options for the second spot for each of the first spot options. If there are three places, it has to consider n different options for the first one. 
 
 Each of these options finally result in a puzzle with two vacant locations and `n*n` possible solutions. Additionally, our algorithm executes a depth- first search through all possible solutions of the puzzle by checking for each number from one to nine for the number of squares that need to be filled. It initially checks whether or not it is okay to assign a number to a square and in the case that the number assigned is right, further possibilities are checked with the next column. 
 
 However, before actually assigning a number, we confirm that the same number is not present in the current row, column or 3 by 3 square. in the case that the assignment made was not right, backtracking is performed to check for the next value for a current empty cell and if none of the no.s between 1-9 lead to a solution, the program returns false. The depth of the graph in this case is the no. of squares that need to be filled and with a depth of m and corresponding branch factor of n, determining a solution has a worst case of O (n ^ m).
 
### Space Complexity:
The Data Structure that we used in our algorithm in recursion (Recursive Backtracking). Ideally, the recursion stack, which is N*N levels deep, and in which case we used a 9*9 int array to store all elements of the sudoku, is utilized as an auxiliary space. In the case of our 9*9 sudoku puzzle, all the 81 cells must have assigned valid values, but only one cell is filled at each level. As a result, the space complexity is O(M).


