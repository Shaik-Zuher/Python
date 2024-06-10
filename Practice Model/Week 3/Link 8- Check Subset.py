def subset(lenA, A, lenB, B):
    result = True
    for num in A:
        if num not in B:
            result = False
    return result
        
for test_case in range(int(input())):
    lenA = int(input())
    A = set(input().split())
    lenB = int(input())
    B = set(input().split())
    if (lenA > lenB):
        print(False)
    else:
        print(subset(lenA, A, lenB, B))
