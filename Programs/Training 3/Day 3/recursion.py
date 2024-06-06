#sudoko solver
#take 4*4 matrix first print it using recursion
'''
matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
def printer(x,y,matrix):
    if  x==len(matrix):
        return
    print(matrix[x][y],end=" ")
    Nx,Ny=-1,-1
    if y==len(matrix)-1:
        Nx=x+1
        y=0
        print()
    else:
        Nx=x
        Ny=y+1
    printer(Nx,Ny,matrix)
printer(0,0,matrix)
'''
#practice----------------------------print matrix elemnts in rverse using recursion
class Solution(object):
    def isPossible(self, board, x, y, value):
        # Same row checking 
        for col in range(9):
            if board[x][col] == str(value):
                return False
 
        # Same col checking
        for row in range(9):
            if board[row][y] == str(value):
                return False
 
        # Same 3 * 3 matrix checking 
        topRow = (x // 3) * 3 
        topCol = (y // 3) * 3 
 
        for i in range(3):
            for j in range(3):
                if board[topRow + i][topCol + j] == str(value):
                    return False
        return True
 
def solveThis(self, x, y, board):
    #print(x, y, board)
    if x == 9:
        return True
 
    nextX, nextY = -1, -1 
 
    if y == 8:
        nextX = x + 1 
        nextY = 0 
    else:
        nextX = x 
        nextY = y + 1
 
    if board[x][y] != ".":
        return self.solveThis(nextX, nextY, board)
 
 
    for value in range(1, 10):
        if self.isPossible(board, x, y, value) == True:
            board[x][y] = str(value)
            result = self.solveThis(nextX, nextY, board)
            if result == True:
                return True
            board[x][y] = "."
 
    return False
 
def solveSudoku(self, board):
    self.solveThis(0, 0, board)

