#1.Recursive relation  2.Baseend
'''
def fact(n):
    if(n==0):
        return 1
    else:
        return n*fact(n-1)
print(fact(3))

def fibnocci(m):
    if(m==0):
        return 0
    if(m==1):
        return 1
    return fibnocci(m-1)+fibnocci(m-2)
print(fibnocci(3))
'''
#2.write a recursive program to print digits of number in reverse order
'''
def digit(d):
    if d==0:                   tip:think about basecase(end)==0
        return
    print(d%10)
    return digit(d//10)
digit(1235)
'''
#3.write the recursion function count no of digits of number
'''
def county(d):
    if d==0:
        return 0
    return 1+county(d//10)   #understnd recursive relation base and keep in track about the + or* 
print(county(12345))
'''
#4.write recursive function to calculate sum of digits of number
'''
def addition(d):
    if d==0:#base end is 0
        return 0#first got to print sum(last+last-1+last-2....
    return d%10+addition(d//10)
print(addition(12345))
'''
#5.Niel Arm Strong
def cod(n):
    if n==0:
        return 0
    return 1+cod(n//10)
count=cod(153)
def arm(num,c):
    if num==0:
        return 0
    return (num%10)**c+arm(num//10,c)
if(153==arm(153,count)):
    print("Arm strong")
else:
    print("Not Arm Strong")

