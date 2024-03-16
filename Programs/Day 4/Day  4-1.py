#Functions are 2 types --lamda,map function
'''
syntax lamda
c=lamda x: operation
#here x is parameter and operation is your operation
d=lamda x,y:opeartion #has 2 arguments
example:
    c=lamda x,y:x**y
    c(2,3)
'''
'''
syntax map
map(function,iteratable)
ex:b=list(map(lamda x:x//10,[90,88,90]))
'''
'''
#sets-creation,add,update,discard
set={1,"gowtham","swetha","teddy",20}
print(set)
set.add(24)
set.update([90,56,77])
set.remove(20)
set.discard(24)
print(set.pop())
set2=set
fs=frozenset(set2)
print(set2)
'''
#2,0,2024,0,40,2030,0
list=[2,0,2024,0,40,2030,0]
list2=[]
for i in range(0,len(list)):
    if(list[i]!=0):
        list

    

    
