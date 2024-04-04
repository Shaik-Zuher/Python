list=[12,42,23,96,7,18,10,133]
mini=list[0]
maxi=list[0]
minid=0
maxid=0
for i in range(0,len(list)):
    if(mini>list[i]):
        mini=list[i]
        minid=i
    if(maxi<list[i]):
        maxi=list[i]
        maxid=i
sum=minid+maxid
diff=maxid-minid
list[minid]=diff
list[maxid]=sum
print(list)
