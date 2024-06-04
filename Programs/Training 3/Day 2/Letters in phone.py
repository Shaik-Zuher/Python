d={
    "2":"abc",
    "3":"def",
    "4":"ghi",
    "5":"jkl",
    "6":"mno",
    "7":"pqrs",
    "8":"tuv",
    "9":"wxyz"
    }
#first try to print "2"->abc,"3"->efg
'''
def pt(i,s):
    if i==len(s):
        return
    print(s[i],"-->",d[s[i]])
    pt(i+1,s)
pt(0,"234")
'''
#now try to print in 2 a,b,c
'''
def pt(i,s):
    if i==len(s):
        return
    ch=s[i]
    for j in d[ch]:
        print(j)
    pt(i+1,s)
pt(0,"234")
'''
res=[]
sub=[]
def backtrack(index,s,sub):
    if index>=len(s):
        res.append("".join(sub))
        return
    ch=s[index]
    for i in d[ch]:
        sub.append(i)
        backtrack(index+1,s,sub)
        sub.pop()#responsible for backtracking
backtrack(0,"234",sub)
print(res)

