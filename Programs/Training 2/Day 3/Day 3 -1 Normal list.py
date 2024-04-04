#l=[2,1,2,2,0,1,2,0,0,1,1]
#otput must be 00011112222
#Don't use ssorting or extra spaces
#usng variables doenst occupy that much space
l=[2,1,2,2,0,1,2,0,0,1,1]
c0=0
c1=0
c2=0
for i in l:
    if i==0:
        c0+=1
    if i==1:
        c1+=1
    if i==2:
        c2+=1
index=0
while c0>0:
    l[index]=0
    c0-=1
    index+=1
while c1>0:
    l[index]=1
    c1-=1
    index+=1
while c2>0:
    l[index]=2
    c2-=1
    index+=1
print(l)
