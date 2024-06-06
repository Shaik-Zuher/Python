def isPossible(x1, y1, x2, y2, N):
    if x1 < 0 or y1 < 0 or x1 >= N or y1 >= N:
        return False 
    elif x1 == x2 and y1 == y2:
        return True 
 
    dx = []
    dy = []
    for i in range(8):
        newX = x1 + dx[i] 
        newY = y1 + dy[i]
        result = isPossible(newX, newY, x2, y2, N)
        if result == True:
            return True 
    return False
 
 
result = isPossible(x1, y1, x2, y2, N)
if result == True:
    print("Can reach")
else:
    print("Cannot reach")
