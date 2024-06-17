# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
d=defaultdict(list)
n,m=map(int,input().split())
for i in range(1,n+1):
    a=input()
    d[a].append(i)
arr=[]
for j in range(m):
    b=input()
    arr.append(b)
for i in arr:
    if i in d:
        for j in d[i]:
            print(j,end=" ")
        print()
    else:
        print(-1)
