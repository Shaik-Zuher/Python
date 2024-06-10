#longest common subsequence
##############lcs concept
###############Include exclude concept remember this
#leetcode
#this can be also told as how many minimum characters to delete to convert s1 into s2
#i.e(s1==s2) so for this just remove non subsequence i.e ans=(m+n)-len(lcs)*2
text1,text2="abcdef","def"
#recursion
def recur(s1,s2,i,j):
    #basecase any hits return
    if i==len(s1) or j==len(s2):
        return 0
    #if equal add 1 and msx from remaining string(******************key)
    if s1[i]==s2[j]:
        res=1+recur(s1,s2,i+1,j+1)
        return res
    case1=recur(s1,s2,i+1,j)#case if we can increase index of s1
    case2=recur(s1,s2,i,j+1)#case2 increase index of s2 don't think comploexly to check based on lengths
    res=max(case1,case2)
    return res
#print(recur(text1,text2,0,0))
#memoization
#cache must be nsized or m sized
n=len(text1)
m=len(text2)
cache = [[-1] * m for i in range(n)]
#what ever right in second in basecase must be columns
print(cache)
def memoizationApproach(index1, index2):
    if index1 == n or index2 == m:
        return 0 
    elif cache[index1][index2] != -1:
        return cache[index1][index2]
    elif text1[index1] == text2[index2]:
        cache[index1][index2] = 1 + memoizationApproach(index1 + 1, index2 + 1)
        return cache[index1][index2] 
    choice1 = memoizationApproach(index1 + 1, index2)
    choice2 = memoizationApproach(index1, index2 + 1)
    cache[index1][index2] = max(choice1, choice2)
    return cache[index1][index2]
print(memoizationApproach(0,0))
print(cache)
str1,str2="abc","def"
n=len(str1)
m=len(str2)
def tabulationApproach():
    cache = [[0] * (m + 1) for i in range(n + 1)]
    for index1 in range(n - 1, -1, -1):
        for index2 in range(m - 1, -1, -1):
            if str1[index1] == str2[index2]:
                 cache[index1][index2] = 1 + cache[index1 + 1][index2 + 1]
            else:
                choice1 = cache[index1 + 1][index2]
                choice2 = cache[index1][index2 + 1]
                cache[index1][index2] = max(choice1, choice2)
         
            return cache[0][0]
print(tabulationApproach())   
