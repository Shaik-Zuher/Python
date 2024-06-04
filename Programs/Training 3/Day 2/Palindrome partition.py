s="ab"
res=[]
sub=[]
def palindrome(index,sub):
    if index>=len(s):
        res.append(sub[:])
        return
    for i in range(index,len(s)):
        part=s[index:i+1]
        if part==part[::-1]:
            sub.append(part)
            palindrome(i+1,sub)
            sub.pop()
palindrome(0,sub)
print(res)
