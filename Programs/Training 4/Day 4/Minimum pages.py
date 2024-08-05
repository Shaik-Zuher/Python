class Solution:
    
    #Function to find minimum number of pages.
    def findPages(self,n ,arr ,m):
        #code here
        if(m>n):
            return -1
        def condition(mid):
            pages=0
            ns=1
            for i in arr:
                if pages+i<=mid:
                    pages+=i
                else:
                    ns+=1
                    pages=i
                    #contagious remember
                if(ns>m or i>mid):
                    return False
            return True
        s=max(arr)
        e=sum(arr)
        while s<=e:
            mid=s+(e-s)//2
            if condition(mid):
                e=mid-1
            else:
                s=mid+1
        return s
