#checking valid paranthessis
#latest open solud be closed first logic
#identity opeartors is ,is not
#opeartions in,not in
'''
logic is that for example [()]
first only push open brackets in stack stack=[ [,( ]
traverse stack  and check if any elent matchs top of stack if yes pop the stack
at last if pop emty then valid paranthesis or not
'''
s="[{()}]"
stack=[]
def push(sta,data):
    sta.append(data)
def top(sta):
    return sta[-1]
def isempty(sta):
    return len(sta)==0
def check(st):
    for i in range(0,len(s)):
        if s[i] in "[{(":
            push(st,s[i])
        elif (s[i]=="]" and top(st)=="[") or (s[i]==")" and top(st)=="(") or (s[i]=="}" and top(st)=="{"):
            st.pop()
        else:#(if any other thing like nmbers are present)
            break
    if isempty(st)==True:
        print("valid")
    else:
        print("Invalid")
check(stack)
