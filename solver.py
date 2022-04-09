N = 9 #Variable to hold the number of rows and colums

count = 0

'''Determines if on a certain position we can put a number returns 
true if it is possible to put a number and false otherwise
# Checks row then checks the columns '''
def isSafe(sudoku, row, col, num):
    for i in range(9):  #Checking if the same number exists in same row
        if sudoku[row][i] == num:
            return False

    for i in range(9): #Checking if the same number exists in the same column, returning False if it does
        if sudoku[i][col] == num:
            return False

#Checking if the same number exists in the particular 3 by 3 grid
    startRow = row - row % 3  
    startCol = col - col % 3 
    for i in range(3):
        for j in range(3):
            if sudoku[startRow + i][startCol + j] == num:
                return False
    return True   #This would get executed if none of the above condition are satisfied 


#Algorithm to solve the sudoku puzzle
def solveSudoku(sudoku, row, col):
    global count 
    count += 1
    
    if count > 1000:
        return False
    
    #Base condition because we would be using Recursion
    if row== N - 1 and col == N:
        return True

#Moving to the next row when last column is reached
    if col == N:
        row += 1
        col = 0

#Checking if the number is assigned to current position
    if sudoku[row][col] > 0:
        return solveSudoku(sudoku, row, col + 1) #We test out the next column

    #Checking for each number from 1 to 9
    for num in range(1, N + 1):
        if isSafe(sudoku, row, col, num): #Check if it is okay to assign the number 
            sudoku[row][col] = num #Assigning the number in the sudoku
            
            #If the number assigned is correct we would also check for possibilities with next column
            if solveSudoku(sudoku, row, col + 1):  
                return True

        #If our assumption was wrong we would backtrack(by assigning 0 in the given position) and check for the next value 
        sudoku[row][col] = 0 #Backtracking
    return False  


#Function to return the solved sudoku if it is solvable
def solver(sudoku):
    global count

    #If condition to check if sudoku is solvable starting from 0th row and 0th column
    if solveSudoku(sudoku, 0, 0): 
        count = 0
        return sudoku
    else:
        count = 0
        return "no"
    










    
