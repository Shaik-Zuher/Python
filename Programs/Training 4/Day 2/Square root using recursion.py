#square root using binary search
def findSquareRootUsingBS(number):
    left, right = 1,number 
    result = 1 
 
    while left <= right:
        mid = (left + right) // 2 
        if mid * mid <= number:
            result = mid 
            left = mid + 1 
        else:
            right = mid - 1 
 
    return result
 
 
print(findSquareRootUsingBS(49))
print(findSquareRootUsingBS(100))
print(findSquareRootUsingBS(121))
print(findSquareRootUsingBS(125))
print(findSquareRootUsingBS(55))
  
