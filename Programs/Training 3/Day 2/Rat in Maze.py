#problem Directions
'''
Consider a rat placed at (0, 0) in a square matrix of order N * N. It has to reach the destination at (N - 1, N - 1). Find all possible paths that the rat can take to reach from source to destination. The directions in which the rat can move are 'U'(up), 'D'(down), 'L' (left), 'R' (right). Value 0 at a cell in the matrix represents that it is blocked and rat cannot move to it while value 1 at a cell in the matrix represents that rat can be travel through it.
Note: In a path, no cell can be visited more than one time. If the source cell is 0, the rat cannot move to any other cell.

Example 1:

Input:
N = 4
m[][] = {{1, 0, 0, 0},
         {1, 1, 0, 1}, 
         {1, 1, 0, 0},
         {0, 1, 1, 1}}
Output:
DDRDRR DRDDRR
Explanation:
The rat can reach the destination at 
(3, 3) from (0, 0) by two paths - DRDDRR 
and DDRDRR, when printed in sorted order 
we get DDRDRR DRDDRR.
Example 2:
Input:
N = 2
m[][] = {{1, 0},
         {1, 0}}
Output:
-1
Explanation:
No path exists and destination cell is 
blocked.
Your Task:  
You don't need to read input or print anything. Complete the function printPath() which takes N and 2D array m[ ][ ] as input parameters and returns the list of paths in lexicographically increasing order. 
Note: In case of no path, return an empty list. The driver will output "-1" automatically.

Expected Time Complexity: O((3N^2)).
Expected Auxiliary Space: O(L * X), L = length of the path, X = number of paths.

Constraints:
2 ≤ N ≤ 5
0 ≤ m[i][j] ≤ 1
'''
#Explaination
"""
T-top
D-down
R-right
L-left
 lets take 4x4 matrix cordibates will be
  00 01 02 03
  10 11 12 13
  20 21 22 23
  30 31 32 33

lets say rat position is (2,1)cordinate(x,y)
top will be  1,1(x-1,y)
down will be 3,1(x+1,y)
left will be 2,1(x,y-1)
right will be 2,3(x,y+1)
task to move from 0,0 to 3,3

1.pattern here is for every x,y is
top- x-1,y
down- x+1,y
right- x,y+1
left- x,y-1

task to move to last cell which 3,3
2.base case will be
x=n-1 and y==n-1 


lets say rat position is (3,3)cordinate(x,y)
top will be  2,3(x-1,y)
down will be 4,3(x+1,y) # error beacuse that is outside of matrix so this is edge case
in same way cordibate cannot be (-1,-1) so another edge case

3.edge case when outside the matrix
x<0 or x>len(matrix) simmillarly y

4.they want to move if only data in cell is 1 but not 0
so matrux[x][y]==0 then break
another problem is  matrix is 1 1 1 1
                              1 1 1 1
                              1 1 1 1
                              1 1 1 1
1st cordinate moves to down
down moves again to top(1st co)
again from(istco down)  like this infinte loop
so we need to mark visited ones as 0 or we can use boolean matrix
when in it change to true
at last change back to false
"""
path = []
matrix = [[1, 1, 0, 0], [1, 1, 1, 1], [1, 1, 1, 0], [1, 1, 1, 1]]
n = len(matrix)
res=[]
visited=[]
#for some reasons not working visited=[[False]*n]*n #4 boolean matrix
for i in range(n):
    eachRow = []
    for j in range(n):
        eachRow.append(False)
    visited.append(eachRow)
def paths(x,y,matrix,n,path,visited):
    # Border checks
    if x < 0 or x == n or y < 0 or y == n: #3.edge case
        return
    if x==n-1 and y==n-1:#2.basecase
        res.append("".join(path))
        return
    # Condition to check whether we can traverse via those coordinates or not
    if matrix[x][y]==0 or visited[x][y]==True: #4 moving
        return
    visited[x][y]=True #already visited #4
    # Top Direction
    path.append("U")
    paths(x - 1, y, matrix, n, path, visited)
    #you might think to use function paths(x,y,matrix,n,path+D) but how will you backtrack ----hmmmmmm
    #so lets just append and pop
    path.pop()
 
    # Bottom Direction
    path.append("D")
    paths(x + 1, y, matrix, n, path, visited)
    path.pop()
 
    # Left Direction 
    path.append("L")
    paths(x, y - 1, matrix, n, path, visited)
    path.pop()
 
    # Right Direction
    path.append("R")
    paths(x, y + 1, matrix, n, path, visited)
    path.pop()
    visited[x][y]=False #fixing back things #4
paths(0,0,matrix,n,path,visited)
print(res)
