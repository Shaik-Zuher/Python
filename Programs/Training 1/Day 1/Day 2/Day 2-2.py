#1.
'''
i=12345
while (i>0):
    num=i%10
    print(num)
    i=i//10
'''

#2.
'''
i=12345
count=0
while (i>0):
    num=i%10
    count+=1
    i=i//10
print(count)
'''
'''
#3.
#num=int(input("enter number:"))
#sum=0
#while (num>0):
#    i=num%10
#    sum+=i
#    num=num//10
#print(sum)
'''
'''
#4.
#num=int(input("enter number:"))
#mul=1
#while (num>0):
#    i=num%10
#    mul*=i
#    num=num//10
#print(mul)
'''
#5.TAKE an integer as input from user and check whether if number is divisble by sum of digits by not
'''
#number=int(input("enter number:"))
#num=number
#sum=0
#while (num>0):
#    i=num%10
#    sum+=i
#    num=num//10
#print("sum is:",sum)
#if( number%sum==0):
#    print("Harshad")
#else:
#    print("not divisible")
'''

#6.Take a number from user check if the sum of factors of numbers of number is greater than original num if yes print yes else no
'''
number=int(input("enter number:"))
num=number
facts=0
for i in range(1,num):
    if(num%i==0):
        print(i)
        facts+=i
print("factorials sum:",facts)
if(facts>number):
    print("Abundant")
else:
    print("no")
'''

#7.calculate difference sum of numbers divisible by 6 and not divisble by 6 in the range of first 30 numbers
'''
number=6
ds=0
nds=0
i=1
while(i<31):
    if(i%6==0):
        ds+=i
    else:
        nds+=i
    i+=1
print(ds)
print(nds)
if(nds<ds):
     print("difference",ds-nds)
else:
    print("difference",nds-ds)
'''

#8.palindrome
'''
number=int(input("Enter:"))
num=number
result=0
while(num>0):
    rem=num%10
    result=result*10
    result=result+rem
    num=num//10
if(number==result):
    print("palindrome")
else:
    print("not palindrome")
'''

#9.Niel Arm strong
'''
number=int(input("Enter:"))
i=number
i1=number
count=0
strong=0
while (i>0):
    num=i%10
    count+=1
    i=i//10
while (i1>0):
    numb=i1%10
    arm=numb**count
    i1=i1//10
    strong+=arm
if(number==strong):
    print("armstrong")
else:
    print("not armstrong")
'''
#.10
number=int(input("enter:"))
n=number
n1=number
count=0
exp=0
eum=0
rev=0
new=0
while (n>0):
    rem=n%10
    rev=rev*10
    rev=rev+rem
    n=n//10
while (rev>0):
    new=rev%10
    count+=1
    exp=new**count
    eum+=exp
    rev=rev//10
print(eum)
    

    
