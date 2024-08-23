class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        #check time taken for each car
        #if time taken of one car is less than time taken by next car that means it will meet so this is nge type problem
        #regaradless of positions we need to reach target so sort them in ascending order
        #ex:[[0,4],[2,2][4,1]] 7
        #dist=speed*time -----hehe 
        #dist=target-position//speed
        #time:  28      10     3
        ###fleet =3 because neither of them are less than next
        paths=[i for i in zip(position,speed)]
        paths.sort()
        time=[]
        for i in paths:
            cal=(target-i[0])/i[1]
            time.append(cal)
        s=[]
        for i in range(len(time)-1,-1,-1):
            if not s:
                s.append(time[i])
            elif time[i]>s[-1]:
                s.append(time[i])
        return len(s)
