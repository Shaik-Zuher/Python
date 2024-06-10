# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
countries=[input() for _ in range(n)]
s=set(countries)
print(len(s))
