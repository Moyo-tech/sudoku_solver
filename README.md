# sudoku_solver
Data structure and algorithm used:
Data structure: Recursive Data structure
A recursive data structure is a data structure that consists of parts of smaller or simpler instances of the same data structure. For example, linked lists and binary trees can be viewed as recursive data structures
Algorithm used:
The algorithm we used is the backtracking algorithm
Backtracking is an algorithmic technique that aims to use a brute force approach to get all the solutions to a problem. It consists of building a complete set of solutions in stages. Due to the limitations of the issues, solutions that do not meet them will be removed. 
 It uses the recursive call to build the solution step by step and find the solution set by increasing the level over time.
Essentially, you keep trying numbers in empty spots until there aren't any that are possible, then you backtrack and try different numbers in the previous slots.

Project Description
Sudoku is a logic-based puzzle that plays with numbers from 1 to 9. The puzzle first appeared in a newspaper in France in November 1892. Most of the essays that study Sudoku solvers show different types of Sudoku solvers algorithm. Thanks to its simple rules, it's fascinating and very easy to learn. There are  many now Classic Sudoku including various kinds of Sudoku puzzles,  9X9 grid with given clues, Mini Sudoku consisting of 4X4 ​​or 6X6 size grids in different locations etc. In our project, we focused is mainly on the classic Sudoku that is, the 9X9 grid. 
Each Sudoku puzzle begins with some cells filled in. These numbers are chosen such that there is a unique solution to the Sudoku.
