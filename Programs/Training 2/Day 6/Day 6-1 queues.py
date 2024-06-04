l=[-8,2,3,-6,10]
#window number is 2
#print smaller negative in  every window numbers(i.e in every 2 nubers)
#sliding window pror\tocol 
'''
#not optimal solution
from collections import deque
dq=deque()
dq.append(-8)
dq.append(2)
dq.append(3)
dq.append(-6)
dq.append(10)
ans=deque()
print(dq)
for i in range(0,len(dq)):
    for j in range(i+1,len(dq)):
        if(dq[i]>=0 and dq[j]<0)or(dq[j]>=0 and dq[i]<0) or (dq[i]<0 and dq[j]<0):
            if(dq[i]>dq[j]):
                ans.append(dq[j])
            else:
                ans.append(dq[i])
            break
        else:
            break
print(ans)
'''
#n element window
from collections import deque
dq=deque()
w=2
n=len(l)
for i in range(0,w):#first check window elements
    if l[i]<0:     #adding index
        dq.append(i)
for i in range(w,n):#check other elements
    #print dq elemnets
    if len(dq)==0:
        print(0)
    else:
        print(l[dq[0]])#dq will have only 1 value
    #clearing dq
    while(dq and i-dq[0]>=w):
        dq.popleft()
    if(l[i]<0):
        dq.append(i)
if len(dq)>0:
    print(l[dq[0]])
else:
    print(0)

    
