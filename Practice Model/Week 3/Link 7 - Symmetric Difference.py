# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
en=int(input())
ens=set(map(int,input().split()))
fr=int(input())
frs=set(map(int,input().split()))
s=ens.symmetric_difference(frs)
print(len(s))
