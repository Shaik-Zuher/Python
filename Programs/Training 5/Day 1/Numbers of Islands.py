grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m=len(grid)
        n=len(grid[0])
        result=0
#recursion good when src and dest known
        #all these check if adjacent values are 1 and all adjacent are changed to 0
        def visited(x,y):
            if x<0 or y<0 or x>=m or y>=n or grid[x][y]=="0":
                return
            grid[x][y]="0"
            visited(x-1,y)
            visited(x+1,y)
            visited(x,y-1)
            visited(x,y+1)
        #end grid=[["0","0","0","0","0"],
        #           ["0","0","0","0","0"],
        #           ["0","0","0","0","0"],
        #           ["0","0","0","0","0"]] after first iteration so the same ones cant be checked again
        for i in range(m):
            for j in range(n):
                if(grid[i][j]=="1"):
                    visited(i,j)
                    result+=1
        return result
        
