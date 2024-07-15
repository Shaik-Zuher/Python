'''
Steps by Knight
Given a square chessboard, the initial position of Knight and position of a target. Find out the minimum steps a Knight will take to reach the target position.
Note:
The initial and the target position coordinates of Knight have been given according to 1-base indexing.
Example 1:
Input:
N=6
knightPos[ ] = {4, 5}
targetPos[ ] = {1, 1}
Output:
3
Explanation:
Knight takes 3 step to reach from 
(4, 5) to (1, 1):
(4, 5) -> (5, 3) -> (3, 2) -> (1, 1).
'''
""" 2d matrix
 00 (01) 02 (03) 04  05 
(10) 11  12  13 (14) 15        let 2,2 be initial positon knight can move to positions marked with ()
 20  21 [22] 23  24  25
(30) 31  32  33 (34) 35        directions  are (-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)
 40 (41) 42 (43) 44  45        lets take queue and append position as we need to change position to go to destination and first take current position
 50  51  52  53  54  55        as bfs used gotta take queue for row,col,steps initial steps=0
"""
N=6
knightPos=[4, 5]
targetPos=[1, 1]
def minStepToReachTarget(KnightPos, TargetPos, N):
    #having initial(current) position
    queue=[[KnightPos[0],KnightPos[1],0]]#0 represnts posititon
    #directions
    directions=[[-2, 1],[-1, 2],[1, 2],[2, 1],[2, -1],[1, -2],[-1, -2],[-2, -1]]
    #visited as we don't need to repeat same cells
    visited=set()
    #empty set must be like this
    while len(queue)!=0:
        pos=queue.pop(0)#############
        curow,curcol,step=pos[0],pos[1],pos[2]
        #if current position is target position
        if curow==TargetPos[0] and curcol==TargetPos[1]:
            return step
        #moving in directions
        for d in directions:
            #new cell
            nrow=curow+d[0]
            ncol=curcol+d[1]
            #cell must not be out of bounds(i.e outside boards)
            if nrow>=0 and ncol>=0 and nrow<=N and ncol<=N and (nrow,ncol) not in visited: #becoz we dont want to visit same cell
                visited.add((nrow,ncol))
                queue.append((nrow,ncol,step+1))#appending new pos with steps added
    return -1
print(minStepToReachTarget(knightPos,targetPos,N))
        
