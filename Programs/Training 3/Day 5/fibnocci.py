#print nth fibnoic number using loop
n=int(input("Enter:"))
first=0
second=1
for i in range(0,n):
    third=first+second
    first,second=second,third
print(first)
#fibnoic using recursion
def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return (n-2)+(n-1)
print(fib(n))
