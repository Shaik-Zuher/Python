#1.Write prgram in which you take an integer input from user if integer divisible by 3 and 6 print good number if disible by 2 and 7 print and average number and if divisibe by 4 or 9 print awesome number else print bad number

#Num=int(input("Enter the number:"))
#if Num%3==0&Num%6==0:
#    print("good number")
#elif Num%2==0&Num%7==0:
#    print("average number")
#elif Num%4==0|Num%9==0:
#    print("awesome number")
#else:
#    print("bad number")


#2.Write program to check on road price of bike under conditions:
#if price greater than 72,000 and less than 150000 income tax is 10% of price and insurance is 15% of actual price
#if price greater than 1,50,000 and less than 2,00,000 tax would be 25% and insurance will be 20%
#if price above 2,00,000 then tax will be 35% and insurance will be 28% otherwise min price is 72000 enter valid value
#print onroad price of bike formula is actual price +tax calculated from actual+insurance calculated from actual value

#price=int(input("enter the price:"))
#if price>72000 and price<=150000:
#    b=price+(10/price)*100+(15/price)*100
#   print(b)
#elif price>150000 and price<=200000:
#    b=price+(25/price)*100+(20/price)*100
#    print(b)
#elif price>200000:
#    b=price+(35/price)*100+(25/price)*100
#    print(b)
#else:
#    print("Enter valid value")

#3.check if leap year if year divisible for 4 and not divisible by 100 or if divisble by 400 then call leap

#year=int(input("enter year:"))
#if((year%4==0 and year%100!=0) or year%400):
#    print("leap year")
#else:
#    print("not leap year")

#4.write program to check type of traingle when you take input from user for 3 sides and classify it accordinly into equilator ,isocles,scalar

#sideA=int(input("enter A:"))
#sideB=int(input("enter B:"))
#sideC=int(input("enter C:"))
#
#if sideA==sideB and sideB==sideC and sideC==sideA:
#    print("equilateral triangle")
#elif (sideA==sideB and sideC!=sideA) or (sideA==sideC and  sideB!=sideA) or (sideC==sideB  and sideA!=sideC):
#    print("isocles triangle")
#elif sideA!=sideB and sideB!=sideC:
#    print("scalar triangle")
#else:
#    print("not a triangle")

#5.calculate value of 7! using for

#a=7
#b=1
#for i in range(1,a+1):
#    b*=i
#print(b)

#6.fibnoic series

#first=0
#last=1
#print(first)
#print(last)
#for i in range(0,8):
#   next=first+last
#    print(next)
#    first=last
#    last=next

#7.prime no or not
#prime=int(input("Enter a number:"))
#count=0
#for i in range(1,prime+1):
#    if prime%1==0 and prime%prime==0:
#        count+=1
#if(count!=0):
#    print("prime number")
#else:
#    print("not prime number")
#prime=int(input("enter the number"))
#flag=0
#for i in range(2,prime):
#    if prime%i==0:
#        flag=1
#        break
#if(flag==0):
#    print("prime")
#else:
#    print("Not prime")

#8.calculate the sum of digits of a number which is taken as input frm user
input=int(input("Enter input:"))
b=0
while input>0:
    a=input%10
    b=b+a
    input=input//10
print(b)
