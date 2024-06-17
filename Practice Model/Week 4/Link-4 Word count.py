# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
words=OrderedDict()
for i in range(int(input())):
    s=input()
    if s in words:
        words[s]+=1
    else:
        words[s]=1
print(len(words))
for j in words.values():
    print(j,end=" ")
