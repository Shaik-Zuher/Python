#Recursion to find vowels in word
n=input("Eneter the string:",)
v="AEIOUaeiou"
c=0
def vowels(c,index,n):
    if index==len(n):
        print(c)
        return
    if n[index] in v:
        c+=1
    vowels(c,index+1,n)
vowels(c,0,n)
def vowels1(index,n):
    if index==len(n):
        return 0
    vc=vowels1(index+1,n)
    if n[index] in v:
        vc=1
    return vc
print(vowels1(0,n))
