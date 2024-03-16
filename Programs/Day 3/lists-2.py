list=[22,-1,42,65,1,-4,6]
#write program to find second smallest negative number from list without using methods
def negative():
    mini=list[0]
    for i in range(len(list)):
        if(mini>list[i]):
            mini=list[i]
            index=i
    list2=list.remove(list[index])
    print(list2)
    
negative()
