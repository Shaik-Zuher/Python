#Dynamic programming takes much less spac than backtrack and recursion
#In backtracking we use recursions 2 or more times
#In recursion the main disadvantage is that we have to call same recursions many times which takes a lot of space
#So can't we just use a space to store all recursion values so that next time when same recursion appears so won't need to do same recursions again  to reduce space (hashmaps/dictionaries)
#This process to store recursions  is called as memoization and space is called as cache
#Recursion->Recrsion+cache(memoization)->Tabulation
#######################cache intiaited as cache=[-1]*(n-1)
#Tabulation more advanced than memoization and it it ultimate one
#process for tebulation is from recursion and then use cache in it and then use tabulation
#sometimes result can be large so result can redusced by result%(10^9+7)

# Using Recursion
def findNthTerm(n):
    if n == 1 or n == 2:
        return 1 
 
    result1 = findNthTerm(n - 1)
    result2 = findNthTerm(n - 2)
    return result1 + result2 
 
# Using Memoization 
def findNthTermUsingCache(n, cache):
    if n == 1 or n == 2:
        return 1 
    elif cache[n] != -1:
        return cache[n]
 
 
    result1 = findNthTermUsingCache(n - 1, cache)
    result2 = findNthTermUsingCache(n - 2, cache)
    cache[n] = result1 + result2
    return result1 + result2 
 
# Tabulation approach (Ultimate Dynamic programming solution)
def findNthTermUsingTabulation(n):
    cache = [-1] * (n + 1)
    # Whatever base condition we wrote 
    # recursive solutin, we need to 
    # initialize them 
 
    cache[1] = 1 
    cache[2] = 1 
    # 1 - wherever 'n' is present, replace it with index 
    # 2 - wherever 'functionCall' is there replace it with cache 
 
    for index in range(3, n + 1):
        result1 = cache[index - 1]
        result2 = cache[index - 2]
        cache[index] = result1 + result2
 
    return cache[n]
 
 
 
 
n = 4
 
# cache = [-1] * (n + 1)
# print(findNthTermUsingCache(n, cache))
print(findNthTerm(n))
print(findNthTermUsingTabulation(n))
 
