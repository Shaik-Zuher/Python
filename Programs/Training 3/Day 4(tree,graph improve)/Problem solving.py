#1.Take a input as string tell the number of times shift keyword(keypad) is used
#input:  s="aAwW" output=2
#explaination: from a to A(shift used) 1
#              from w to W(shift used) 1  so total=2
'''

n=input("Enter:")
c=0
for i in range(0,len(n)-1):
    if(n[i]!=n[i+1] and (n[i]==n[i+1].upper() or n[i]==n[i+1].lower())):
       c+=1
print(c)
'''
#2.There are three zones and some stations in zones

#3.path finding
