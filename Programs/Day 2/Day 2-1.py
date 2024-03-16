#pattern
'''
for i in range(1,4):
    for j in range(1,6):
        print("x",end="")
    print("")
'''
'''
r=5
for i in range(1,6):
    for spaces in range(1,r-i+1):
        print(" ",end="")
    for j in range(1,i+1):
        print("x",end="")
    print()
'''
'''
r=4
for i in range(1,5):
    for j in range(1,5):
        if(i==1 or i==r or j==1 or j==r):
            print("x",end="")
        else:
            print(" ",end="")
    print()
count=1
for i in range (1,6):
    for j in range (1,i+1):
        print(count,end="")
        count+=1
    print()
'''
#######################################################################HOMEWORK#########################################################
'''
for i in range (1,10):
    if(i<6):
        for j in range (1,i+1):
            print(i,end="")
        print()
    else:
        for j2 in range(1,10-i+1):
            print(10-i,end="")
        print()
'''
'''
r=4
for i in range(1,r+1):
    for spaces in range(1,r-i+1):
        print(" ",end="")
    for j in range(1,2*i):
        if(i==2 and j==2)or (i==3 and j==3) or(i==3 and j==4) or(i==3 and j==2):
            print(" ",end="")
        else:
            print("x",end="")
    print()
'''
