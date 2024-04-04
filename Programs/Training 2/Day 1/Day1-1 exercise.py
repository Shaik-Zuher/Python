#Find first and last occurance
list=[1,4,4,4,9,13,15,15]

class occurance:
    def first(self):
        s=0
        e=len(list)-1
        t=4
        ans=0
        mid=s+(e-s)//2
        while s<=e:
            if list[mid]==t:
                ans=mid
                e=mid-1
            elif t<list[mid]:
                e=mid-1
            elif t>list[mid]:
                s=mid+1
            mid=s+(e-s)//2
        print(ans)
    def last(self):
        s=0
        e=len(list)-1
        t=4
        ans=0
        mid=s+(e-s)//2
        while s<=e:
            if list[mid]==t:
                ans=mid
                s=mid+1
            elif t<list[mid]:
                e=mid-1
            elif t>list[mid]:
                s=mid+1
            mid=s+(e-s)//2
        print(ans)
occur=occurance()
occur.first()
occur.last()
'''
def last():
    s=0
    e=len(list)-1
    t=4
    ans=0
    mid=s+(e-s)//2
    while s<=e:
        if list[mid]==t:
            ans=mid
            s=mid+1
        elif t<list[mid]:
            e=mid-1
        elif t>list[mid]:
            s=mid+1
        mid=s+(e-s)//2
    print(ans)
last()
def first():
    s=0
    e=len(list)-1
    t=4
    ans=0
    mid=s+(e-s)//2
    while s<=e:
        if list[mid]==t:
            ans=mid
            e=mid-1 
        elif t<list[mid]:
            e=mid-1
        elif t>list[mid]:
            s=mid+1
        mid=s+(e-s)//2
    print(ans)
first()
'''
