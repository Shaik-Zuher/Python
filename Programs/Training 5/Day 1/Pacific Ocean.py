#Backtrack rat in maze we are asked all possible paths so after changed they must be restored to check another possible paths but in this graph we don't care about all possiblities
"""
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.
The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).
The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.
Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.
Example 1:
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean 
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean 
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean 
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean 
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean 
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
        atlantic
        1 2 2 3 5
        3 2 3 4 4
pacific 2 4 5 3 1   atlantic
        6 7 1 4 5
        5 1 1 2 4
        pacific
"""
#we have one boolean matrix with all false which checks if every cell can reach atlantc 
#similary another matrix for pacific
#but checking every cell incerasese time every time we check from source(cell) to dest(ocean) instead lets check dest to src
#condition is from 4 water can go to 3 how about revrse cell can water from greater one so 3 can get frn 4 similarlly 4 can get from 5
##we cant check if anything is going outside the borders always go into ocean so how about using borders as dest
class Solution(object):
    def pacificAtlantic(self, heights):
        m, n = len(heights), len(heights[0])
        pacific = [[False] * n for i in range(m)]
        atlantic = [[False] * n for i in range(m)]
        
        def visitAllNodes(row, col, ocean):
            if ocean[row][col]:
                return 
            ocean[row][col] = True 
            Q = [[row, col]]
            #taking queue becoz graph and checking all adajcent cells one for all
            #checking top,bottom,left,right
            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            while Q:
                curr = Q.pop(0)
                #poping queue
                for direction in directions:
                    newRow = curr[0] + direction[0]
                    newCol = curr[1] + direction[1]
                    #checking f to true
                    # heights[newRow][newCol] >= heights[curr[0]][curr[1] checks adjacents
                    if newRow >= 0 and newCol >= 0 and newRow < m and newCol < n and ocean[newRow][newCol] == False and heights[newRow][newCol] >= heights[curr[0]][curr[1]]:
                        ocean[newRow][newCol] = True 
                        Q.append([newRow, newCol])
                        #appending adjacent cells which are marked as true to be checked next
                
        #usin row can dest has 1st row has pacific and 2nd has atlantic and m is rows
        for row in range(m):
            visitAllNodes(row, 0, pacific)
            visitAllNodes(row, n - 1, atlantic)
        #similarly for columns
        for col in range(n):
            visitAllNodes(0, col, pacific)
            visitAllNodes(m - 1, col, atlantic)
            
        result = []
        #if cell in both matrices are true
        for row in range(m):
            for col in range(n):
                if pacific[row][col] and atlantic[row][col]:
                    result.append([row, col])
        
        return result
