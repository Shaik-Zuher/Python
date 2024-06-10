m=3
n=7
res=[]
matrix=[]
ans=[]
for i in range(m):
    col=[]
    for j in range(n):
        col.append(0)
    matrix.append(col)
#####recursion
def paths(x,y,res,ans,matrix):
    if x==len(matrix)-1 and y==len(matrix[0])-1:
        ans.append(" ".join(res))
        return
    if y==len(matrix[0]) or x==len(matrix):
        return
    res.append("D")
    paths(x+1,y,res,ans,matrix)
    res.pop()
    res.append("R")
    paths(x,y+1,res,ans,matrix)
    res.pop()
#paths(0,0,res,ans,matrix)
#print(len(set(ans)))
''' This acnnot be memoized becuase the solution doesn't return anything so we need to change solution as return something'''
def p(x,y,matrix):
    if x==len(matrix)-1 and y==len(matrix[0])-1:
        return 1
    if y==len(matrix[0]) or x==len(matrix):
        return 0
    a=p(x+1,y,matrix)
    b=p(x,y+1,matrix)
    res=a+b
    return res
#print(p(0,0,matrix))
##memoization
#cache=[-1]*n but as it is 2d keep in loop
cache=[]
for i in range(0,m):
    c=[-1]*n###base ends at n-1 but we want n sized array so *n
    ###############################cache always wants n sized arrays
    cache.append(c)
def pmemo(x,y,matrix):
    if x==len(matrix)-1 and y==len(matrix[0])-1:
        return 1
    elif y==len(matrix[0]) or x==len(matrix):
        return 0
    elif cache[x][y]!=-1:
        return cache[x][y]
    a=pmemo(x+1,y,matrix)
    b=pmemo(x,y+1,matrix)
    cache[x][y]=a+b
    return cache[x][y]
#print(pmemo(0,0,matrix))
########tabulation
def tabulation(m,n):
    #take cache from pmemo
    cache=[]
    #suppeose list=[1,2,3....m](len=m) in tabulation we need to go upto index of len to store last cache value but it will throw index out of range so instead lets just keep  take m+1
    for i in range(m+1):
        c=[0]*(n+1)
        cache.append(c)
    #if x==len(matrix)-1 and y==len(matrix[0])-1:
    #   return 1
    #Tabulation doest have recurson so base case must be stored in last index of cache
    cache[m-1][n-1]=1
    #reverse loop
    for row in range(m-1,-1,-1):
        for col in range(n-1,-1,-1):
            if row==m-1 and col==n-1: #as last value already stored so leave it
                continue
            a=cache[row+1][col]
            b=cache[row][col+1]
            cache[row][col]=a+b
    print(cache)
    #[[28, 21, 15, 10, 6, 3, 1, 0], [7, 6, 5, 4, 3, 2, 1, 0], [1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0]]  in this last is 0 to maitain this we used if condition
    return cache[0][0] # answer stored here
print(tabulation(m,n))

            
'''
 def tabulationApproach():
            cache = []
            for i in range(m + 1):
                row = [0] * (n + 1)
                cache.append(row)
            cache[m - 1][n - 1] = 1 
 
            for row in range(m - 1, -1, -1):
                for col in range(n - 1, -1, -1):
                    if row == m - 1 and col == n - 1:
                        continue 
                    downWay = cache[row + 1][col]
                    rightWay = cache[row][col + 1]
                    cache[row][col] = downWay + rightWay 
            return cache[0][0]
 
        return tabulationApproach()
'''

