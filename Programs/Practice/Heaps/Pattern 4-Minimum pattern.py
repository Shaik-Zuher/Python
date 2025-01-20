##This is minimum type pattern problem which is actually soooo crappy
#Maybe because it always comes with greedy concept This pattern is what which is equal to binary search.
#####This can be identified in question it shown somewhat like priority like i only want latest until current point(gas station refuel) or I want samllest until this point(meeting rooms)
#These pattern usually depend on gut feeling or intitution  and these problems always involve sorting of elemnent
""""""
#In this problem some can only be solved with heap not binary search identify is constarint for bs it is 10^5
##Pattern i observed is like it same as other heap we want some small/big +k what differnt is it usually cntains some 2 arrays or single 2D array like this.
"""Once again saying it requires sorting"""
"""
Meeting rooms2

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1
Input: intervals = [(0,30),(5,10),(15,20)]
Output: 2
Explanation: We need two meeting rooms
room1: (0,30)
room2: (5,10),(15,20)

Example 2
Input: intervals = [(2,7)]
Output: 1
Explanation: Only need one meeting room
"""
"""
We can solve this problem by first sorting all the training sessions according to their start time. So [2, 4] [1,7] [7, 8] [3, 5] becomes [1, 7] [2, 4] [3, 5] [7, 8]
Next we iterate over the sorted training sessions, and we will check if the end time of the earliest ending training session is less than or equal to next training's start time, if thats the case.
It means we can reuse the training room and don't need a new room.
We can use PriorityQueue to solve this problem, as we need to find the earliest ending training session.
We add end time of a training session to the PriorityQueue. 
"""
#First iterate through intervals and add to heap but before that check if any room in heap is becoming free(usually check shortest time room)
#If we short time room is below current room remove the short time room and add current one soooo good
from heapq import *
class Solution:
    def minMeetingRooms(self, start, end):
        intervals=[[start[i],end[i]] for i in range(len(start))]
        #These problem we always need to sort
        intervals.sort()
        heap=[]
        for i in intervals:
            #check if any short time room is now available before current meeting which is usually fisrt one 
            if heap:
                if heap[0]<=i[0]:
                    heappop(heap)
            #adding to heap
            heappush(heap,i[1])
        return len(heap)

"""
871. Minimum Number of Refueling Stops

A car travels from a starting position to a destination which is target miles east of the starting position.
There are gas stations along the way. The gas stations are represented as an array stations where stations[i] = [positioni, fueli] indicates that the ith gas station is positioni miles east of the starting position and has fueli liters of gas.
The car starts with an infinite tank of gas, which initially has startFuel liters of fuel in it. It uses one liter of gas per one mile that it drives. When the car reaches a gas station, it may stop and refuel, transferring all the gas from the station into the car.
Return the minimum number of refueling stops the car must make in order to reach its destination. If it cannot reach the destination, return -1.
Note that if the car reaches a gas station with 0 fuel left, the car can still refuel there. If the car reaches the destination with 0 fuel left, it is still considered to have arrived.

Example 1:
Input: target = 1, startFuel = 1, stations = []
Output: 0
Explanation: We can reach the target without refueling.

Example 2:
Input: target = 100, startFuel = 1, stations = [[10,100]]
Output: -1
Explanation: We can not reach the target (or even the first gas station).

Example 3:
Input: target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
Output: 2
Explanation: We start with 10 liters of fuel.
We drive to position 10, expending 10 liters of fuel.  We refuel from 0 liters to 60 liters of gas.
Then, we drive from position 10 to position 60 (expending 50 liters of fuel),
and refuel from 10 liters to 50 liters of gas.  We then drive to and reach the target.
We made 2 refueling stops along the way, so we return 2.
 
Constraints:
1 <= target, startFuel <= 109
0 <= stations.length <= 500
1 <= positioni < positioni+1 < target
1 <= fueli < 109
"""
#This one is actually good i like it
#Look we have 2d array
######This uses Idea of time machine(doraemon wowoooo)
"""
##So basically I am going through points to reach destination and using my petrol without refueling
##Once out i will check past stations which has most fuel(there can be extra left at end right) and time travel to that fuel 
##So i will maintain max heap and add all those to it once i run out i will take(time travel)
"""
# Initial     positions           target
# fuel(10)  [1,60],[4,1],[30,2]    100
# car         
#           car(fuel is 9)(current fuel-position)     memory=[60]
#                  car(fuel is 5)                     memory=[60,1]
#                       car stops in middle so i will check my memory my first stop has more fuel
#                       time travel tell my self hey add fuel here and return
#                          car
#                                   car(imp this must be checked if car can reach target not upto last gas station)
class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        time_travel=[]
        ans=0
        intial=0 #not needed written for understanding
        i=0
        #for i in stations:   #Dont use for loop because we are using if else loop when fuel to reach station is empty it goes to else  and not added to memory
        while i<len(stations):  
            dist=stations[i][0]-intial
            if startFuel-dist>=0:
                heappush(time_travel,-stations[i][1])
                i+=1
            else:
                if not time_travel: #no stations
                    return -1
                else:
                    startFuel+=-heappop(time_travel)
                    ans+=1
        #lastly check if able to reach target
        while startFuel-target<0: #while because maybe not adding only one will be effctive
            if not time_travel:
                return -1
            startFuel+=-heappop(time_travel)
            ans+=1
        return ans
    ##Actually we can use for loop if wise enough
    def AnotherminRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        time_travel=[]
        ans=0
        for i in stations:#LOOK FOR
            if startFuel-i[0]<0:
                if not time_travel: #no stations
                    return -1
                else:
                    startFuel+=-heappop(time_travel)
                    ans+=1
            heappush(time_travel,-i[1])##Add regardless but at atlast if done at first we might add future stations not good
        #lastly check if able to reach target
        while startFuel-target<0: #while because maybe not adding only one will be effctive
            if not time_travel:
                return -1
            startFuel+=-heappop(time_travel)
            ans+=1
        return ans

                
