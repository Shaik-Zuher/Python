# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
d=deque()
for i in range(int(input())):
    x=list(input().split())
    if(x[0]=="append"):
        d.append(int(x[1]))
    elif(x[0]=="popleft"):
        d.popleft()
    elif(x[0]=="pop"):
        d.pop()
    else:
        d.appendleft(int(x[1]))
for i in d:
    print(i,end=" ")
