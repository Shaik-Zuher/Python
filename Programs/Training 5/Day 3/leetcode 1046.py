#we need to remove stones which are maximum and smash them
from heapq import heapify,heappush,heappop
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        nums=[]
        heapify(nums)
        for ele in stones:
            heappush(nums,-ele)
        if(len(nums)==1):
            return -nums[0]
        print(nums)
        while len(nums)>1:
            y=-heappop(nums)
            x=-heappop(nums)
            if(x==y):
                continue
            elif(x!=y):
                heappush(nums,-(y-x))
        if(len(nums)==0):
            return 0
        return -nums[0]
