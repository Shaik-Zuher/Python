#given stack=[2,1,5,6,2,3]
'''#h be height of histogram
         h
      h  h
      h  h    
      h  h     h
h     h  h  h  h
h  h  h  h  h  h
2  1  5  6  2  3
'''
#find the maximum area of histogram or rectangle area=l*b
#but here is some wahat different logic
#In this Histogram the smaller ones are also presnt in preious or next one
'''#h be height of histogram
         h
      h  h
      h  h    
      h  h     h
h     h  h  h  h
1  1  1  1  1  1  #this whole will be breadth of 1
2  1  5  6  2  3
'''
#to solve this don't use count but obbserve where range of rect ends it ends if next rectangle is smaller so use previous smallest and next smallest
'''#h be height of histogram
         h
      h  h
      h  h    
      h  h     h
h     h  h  h  h
h  h  h  h  h  h
2  1  5  6  2  3
0  1  2 3   4  5--indexes
'''
#formula is breadth=next(index of next samll)-prev(index of prev small)-i[b=n-p-i]  #all -1 in next must be rpelsced iwth n(number of elements
l=[2,1,5,6,2,3]
def top(s):
    return s[-1]
def prevsmall(s):
    n=len(s)
    answer=[0]*n#as list must not be empty or else throws error
    stack=[-1]
    for i in range(0,n):
        current=s[i]
        while top(stack)!=-1 and top(stack)>=current:
            stack.pop()
        answer[i]=top(stack)#top of stack must be saved
        stack.append(current)
    return answer
def nextsmall(s):
    n=len(s)
    ans=[0]*n
    stack=[-1]
    for i in range(n-1,-1,-1):
        current=s[i]
        while top(stack)!=-1 and top(stack)>=current:
            stack=[-1]
        ans[i]=top(stack)
        stack.append(current)
    return ans
def area(s):
    n=len(s)
    nex=nextsmall(s)
    prev=prevsmall(s)
    area=[]
    for i in range(0,len(nex)):
        if nex[i]==-1:
            nex[i]=n
    print(nex)
    print(prev)
    print(s)
    for i in range(0,n):
        breadth=nex[i]-prev[i]-i
        ar=s[i]*breadth
        area.append(ar)
    print(area)
area(l)
