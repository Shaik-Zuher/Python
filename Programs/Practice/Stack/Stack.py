#Motonic stack is tack where elements are ascending or descending order
#Next greater,Next smaller,prev greater etc 
#####We have 3 types of next element tracker
"""1.First next larger element"""
stack=[12,44,1,7,3,9]
#if no ele either 0 or -1
#ans=[44,-1,7,9,9,-1]
s=[-1]#default array as it always starts with -1
ans=[0]*len(stack)
for i in range(len(stack)-1,-1,-1):
    while s[-1]!=-1 and stack[i]>=s[-1]:###this is main logic our stack always has greater eles when current ele is greater elements in stack removed until -1
        s.pop()
    ans[i]=s[-1]
    s.append(stack[i])
print(ans)
###One of variation said that the array is cyclic then just append stack to same stack and follow same technique
"""2.Immediate next greater element"""
stack=[12,44,1,7,3,9]
#if no ele either 0 or -1
#ans=[44,-1,7,-1,9,-1]
s=[-1]#default array as it always starts with -1
ans=[0]*len(stack)
for i in range(len(stack)-1,-1,-1):
    while s[-1]!=-1 and stack[i]>=s[-1]:###this is main logic our stack always has greater eles when current ele is greater elements in stack removed until -1
        s=[-1]##allremoved because immediate checked
    ans[i]=s[-1]
    s.append(stack[i])
print(ans)
"""3.Most graetest element"""
stack=[12,44,1,7,3,9]
#ans=[44,9,9,9,9,0]
##for these types generally use prefix max or suffix max
ans=[0]
for i in range(len(stack)-1,-1):
    mx=max(ans[0],stack[i])
    ans.insert(0,mx)
print(ans)
#####This used in traping rain water and rectangle
