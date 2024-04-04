list=[22,-1,42,65,1,-4,6]
#write program to find second smallest negative number from list without using methods
'''
def negative():
    mini=list[0]
    for i in range(len(list)):
        if(mini>list[i]):
            mini=list[i]
            index=i
    list2=list.remove(list[index])
    print(list2)
    
negative()
'''
def neagtive():
    mini=99
    mini1=99
    for i in list:
        if(mini>i):
            mini1=mini
            mini=i
    print(mini1)
neagtive()
    
