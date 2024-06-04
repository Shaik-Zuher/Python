#lets say list=[2,14,16,1,4,12] is stack
#its easy in list but we must do in stack
#The logic is every time end will always be -1.So lets create stack with start as -1 
#1.output must be [14,16,-1,4,12,-1] ie every element must be compared with next one if greater then replaces else -1(compare with only next number not all numbers)
#######might be confsuing just remeber you are doing print,insert,compare########draw a diagram and thing anout logic carefully you can do it buddy
'''
lis=[2,14,16,1,4,12]
def top(s):
    return s[-1]
def printer(s):
    n=len(s)
    ans=[0]*n#list where pop values are stored#run to see reson for writing like this
    print(ans)
    stack=[-1]#initially keep -1 as last element is always -1 and we are iterating in back(laugh emoji)
    for i in range(n-1,-1,-1):#this is reverse looping
                #lastvalue treated as started,firstvalue tretaed as first,step which is jumping i.e if n-1=3 then value 2
    #if step is 2 and n-1=3 the next value is 1 this is how it works
        current=s[i]#in first iteration  it is 12
        while top(stack)!=-1 and top(stack)<=current:#for first iteration top is -1#this checks if top is -1 or nextval in output(pop.next(here it is previous value) less than current value. 
            stack.pop()
             #stack=[-1]--you can also use this
            #let me phrase as the stack has[-1] the while loop skipped so value[-1] can be printed next so top now becomes 12 and then add
          ##########the values must be skipped if satisfied so it can be printed-Main Logic############otherwise keeping poping so stack becomes -1
        ans[i]=top(stack)#for first ieration ans=[0,0,0,0,0-,1]
        #print(ans)
        stack.append(current)#first iteration 12 added to stack
        #print(stack)
    return ans
print(printer(lis))
'''
'''
#2.output must be [-1,-1, 1, -1, -1, -1] ie every elment must be compared with next one if smaller then replaces with nxt number else -1(compare with only next number not allnumbers)
l=[2,14,16,1,4,12]
def top(s):
    return s[-1]
def nextsmaller(s):
    n=len(s)
    ans=[-1]*n
    stack=[-1]
    for i in range(n-1,-1,-1):
        current=s[i]
        while top(stack)!=-1 and top(stack)>=current:
            stack=[-1]
        ans[i]=top(stack)
        stack.append(current)
    return ans
print(nextsmaller(l))
###For previous just loop changed thats all buddy
'''
'''
#3.every elment must be compared with prvious one if smaller then replaces with previous number else -1(compare with only prvious number not allnumbers)
l=[2,14,16,1,4,12]
def top(s):
     return s[-1]
def prevlarg(s):
    n=len(s)
    ans=[0]*n
    stack=[-1]
    for i in range(0,n):
        current=s[i]
        while top(stack)!=-1 and top(stack)>=current:
            stack.pop()
        ans[i]=top(stack)
        stack.append(current)
    return ans
print(prevlarg(l))
'''
#4.every elment must be compared with prvious one if larger then replaces with previous number else -1(compare with only prvious number not allnumbers)

l=[2,14,16,1,4,12]
def top(s):
     return s[-1]
def prevlarg(s):
    n=len(s)
    ans=[0]*n
    stack=[-1]
    for i in range(0,n):
        current=s[i]
        while top(stack)!=-1 and top(stack)<=current:
            #stack.pop()
             stack=[-1]
        ans[i]=top(stack)
        stack.append(current)
    return ans
print(prevlarg(l))

