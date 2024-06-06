matrix=[[1,1,1,1,0,1],
        [0,1,1,0,1,0],
        [1,0,1,1,0,1],
        [0,1,1,0,1,0],
        [1,1,1,0,0,1]]
r=len(matrix)
c=len(matrix[0])
j=-1
cost=0
for k in range(0,r):
    for i in range(0,r):
        if(k<c):
            cost+=matrix[i][k]
    print(cost)
    cost=0
print(cost)
