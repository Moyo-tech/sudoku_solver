# Project Title: Sudoklver

## Team Members:
-Moyosore Weke
-Testimony Adeyemi
-Petronalla 
-Topister Onyango
-Eleaanor Wepnog

## Data structure and algorithm used:**
- Data structure: Recursion and 2D arrays
  - We used a recursive data structure because we designed the algorithm in a way that it calls itself, Recursion is the process whereby a function calls itself. We are also storing the matrix of the board, cells and values in a 2D-array

- Algorithm: Backtracking Algorithm
  - Backtracking is an algorithmic technique that aims to use a brute force approach to get all the solutions to a problem. It uses the recursive call to build the solution step by step and find the solution set by increasing the level over time. Essentially, you keep trying numbers in empty spots until there aren't any that are possible, then you backtrack and try different numbers in the previous slots. This is a better optimized algorithm than the naive approach where you just try every number 
  - How It works in simpler logic
      - A digit in the wrong location often quickly shows that the solution is infeasable. With n entries left, if there are no entries, n = 0, left, we are finished, indicate succes;
otherwise, find a square that is not yet filled, and
for each digit from 1 to 9,
place the digit in the digit in that square and see whether the the solution is feasible, and if so call backtracking algorithm recursively, where
if the algorithm indicates success, we are finished,
otherwise, try the next digit; and
if no digit works, there is no solution.


**Project Description**
Sudoku is a logic-based puzzle that plays with numbers from 1 to 9. The puzzle first appeared in a newspaper in France in November 1892. Most of the essays that study Sudoku solvers show different types of Sudoku solvers algorithm. Thanks to its simple rules, it's fascinating and very easy to learn. There are  many now Classic Sudoku including various kinds of Sudoku puzzles,  9X9 grid with given clues, Mini Sudoku consisting of 4X4 ​​or 6X6 size grids in different locations etc. In our project, we focused is mainly on the classic Sudoku that is, the 9X9 grid. 
Each Sudoku puzzle begins with some cells filled in. These numbers are chosen such that there is a unique solution to the Sudoku.
The sudoku solver aims to help players of sudoku's solve this puzzel in a much shorter time that they would have spent. Also most people who play the sudoku games which are at the back of the newspaper often have to wait for the results to come in the next day so therefore the solver will be there for them to easily to check their solutions early to know if there are right or wrong.
