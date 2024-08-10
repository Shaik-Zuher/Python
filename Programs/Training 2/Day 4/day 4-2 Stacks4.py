#################Find max area of rect
#given stack=[2,1,5,6,2,3]
'''#h be height of histogram
         h
      h  h
      h  h    
      h  h     h
h     h  h  h  h
h  h  h  h  h  h
2  1  5  6  2  3
'''
#find the maximum area of histogram or rectangle area=l*b
#but here is some wahat different logic
#In this Histogram the smaller ones are also presnt in preious or next one
'''#h be height of histogram
         h
      h  h
      h  h    
      h  h     h
h     h  h  h  h
1  1  1  1  1  1  #this whole will be breadth of 1
2  1  5  6  2  3
'''
#to solve this don't use count but obbserve where range of rect ends it ends if next rectangle is smaller so use previous smallest and next smallest
'''#h be height of histogram
         h
      h  h
      h  h    
      h  h     h
h     h  h  h  h
h  h  h  h  h  h
2  1  5  6  2  3
1  2  3  4  5  6--indexes
'''
#formula is breadth=next(index of next samll)-prev(index of prev small)-i[b=n-p-i]  #all -1 in next must be rpelsced iwth n(number of elements
l=[2,1,5,6,2,3]
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        nse=[]
        pse=[]
        s=[[-1,len(heights)]] ######if we dont have next small it means its total upto length not -1
        for i in range(len(heights)-1,-1,-1):
            while len(s)!=1 and s[-1][0]>=heights[i]:
                s.pop()
            nse.insert(0,s[-1])
            s.append([heights[i],i])
        s=[[-1,-1]]#if wwe dont have value then -1
        for i in range(len(heights)):
            while len(s)!=1 and s[-1][0]>=heights[i]:
                s.pop()
            pse.append(s[-1])
            s.append([heights[i],i])
        marea=0
        for i in range(len(heights)):
#usually len of bar(index(1)=1) tends to from 1 to 6 so casually we can say len=6 units but index starts from 0 so breadth=6-1+1(index fixing)
            area=(nse[i][1]-(pse[i][1]+1))*heights[i]
            marea=max(marea,area)
        return marea
sol=Solution()
print(sol.largestRectangleArea(l))
#####Super funky and funnily this is brute force one hahahahahahahah(6098ms) nearly
#####One pass approach i.e using only one stack
l=[2,1,5,6,2,3]
#stack=[[-1,-1]] initial
#normally add elements stack=[[-1,-1],[2,0(index)]]
#for [2,0] can i say that [-1,-1] is previous smaller  but next smaller is still mystry
#append nxt value stack=[[-1,-1],[2,0(index)],[1,1]]
#[1,1] smaller than prev [2,0]-so for it nextsamll is [1,1] and prev small is its prev value in stack 
#so ill pop the value and use prev,next value to find area im going to use this mechanism
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack=[[-1,-1]] #inital
        marea=0
        for i in range(len(heights)):
            #In terms of first iteration
            #heights[i]=1 and stack=[[-1,-1],[2,0]]
            while len(stack)!=1 and stack[-1][1]>=heights[i]:#our condition 
                prev=stack.pop()#[2,0]
                area=(i-(stack[-1][1]+1))*prev[0]#nextsmall index-prevsmall index +1(index fix) *height of bar
                marea=max(area,marea)
            stack.append([heights[i],i])#usual appends
        #after all adds stack not empty yet
        #stack will have elements which has next small as full length
        while len(stack)!=1:
            prev=stack.pop()
            area=(len(heights)-(stack[-1][1]+1))*prev[0]
            marea=max(area,marea)
        return marea
sol=Solution()
print(sol.largestRectangleArea(l))
#this is optimal one
