#In python  we can implement stack using lists (sounds funny)
#basic Static opeartions
'''
Stack=[]
def push(data):
    Stack.append(data)
print("Initially Stack",Stack)
def top():#top not equal to pop as pop removes element but top gives last inserted element but still keeps in stack
    return Stack[-1]
#stack display function
#before that must check if stack is empty
def isempty(s):
    if(len(s)==0):
        return True
    else:
        return False
def display(s):
    while isempty(s)!=True:
        print(top())
        s.pop()
push(0)
push(1)
push(2)
push(3)
print("After pushing Stack",Stack)
Stack.pop()
print("After poping Stack:",Stack)
print("Last inserted element",top())
print(Stack)
display(Stack)
'''
#print stack elements in revrse(extra space) also called as implment queue using stacks
'''
stack=[]
def push(s,data):
    s.append(data)
def top(s):
    return s[-1]
push(stack,1)
push(stack,2)
push(stack,3)
push(stack,4)
push(stack,5)
new=[]
def isempty(s):
    return len(s)==0
def display(s):
    temp=s
    while isempty(temp)!=True:
        print(top(temp))
        temp.pop()
def reverse(s):
    while isempty(s)!=True:
       push(new,s.pop())
reverse(stack)
display(new)
'''
#print stack elements in revrse(extra space) 
      
