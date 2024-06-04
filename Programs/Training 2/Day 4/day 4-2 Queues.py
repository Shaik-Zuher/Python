#queue has append left and pop left
#python has inbuit dequeue which helps in append left and pop left
'''
from collections import deque #important
dq=deque()
dq.append(10)
dq.append(20)
dq.append(30)
dq.append(40)
dq.append(50)
print(dq)
dq.appendleft(1)
print(dq)
dq.popleft()
dq.popleft()
print(dq)
'''
#revere elemnts of queue
'''
from collections import deque #important
s=[]
dq=deque()
dq.append(10)
dq.append(20)
dq.append(30)
dq.append(40)
dq.append(50)
print(dq)
dq.appendleft(1)
print(dq)
dq.popleft()
dq.popleft()
for i in range(len(dq)):
    s.append(dq.pop())
print(s)
'''
'''
for i in range(len(s)):
    dq.append(s.pop)
'''
#reverse half elements of queue
'''
from collections import deque 
s=[]
ele=[]
dq=deque()
dq.append(10)
dq.append(20)
dq.append(30)
dq.append(40)
dq.append(50)
print(dq)
k=int(input("Enter Number:"))
for i in range(k):
    ele=dq.popleft()
    s.append(ele)
while(len(s)!=0):
    dq.append(s.pop())
for i in range(len(dq)-k):
    dq.append(dq.popleft())
print(dq)
'''
from collections import deque 
s=[]
ele=[]
dq=deque()
dq.append(10)
dq.append(20)
dq.append(30)
dq.append(40)
dq.append(50)
mq=deque()
print(dq)
k=int(input("Enter Number:"))
for i in range(k):
    ele=dq.popleft()
    s.append(ele)
print(dq)
while(len(s)!=0):
    mq.append(s.pop())
for i in range(len(dq)):
    mq.append(dq.popleft())
print(mq)
