##This is minimum type pattern problem which is actually soooo crappy
#Rememebr most interval type questions are this pattern
#Maybe because it always comes with greedy concept This pattern is what which is equal to binary search.
#####This can be identified in question it shown somewhat like tasks have priority(sheduling type problems) like i only want latest until current point(gas station refuel) or I want samllest until this point(meeting rooms)
#These pattern usually depend on gut feeling or intitution  and these problems always involve sorting of elemnents
"""
Tip: When ever minimum is given in question first see if there is any monotoic nature
If no check greddy am i choose what is best while making decision--After that check heap(Because greedy comes with heap most time)
"""
#In this problem some can only be solved with heap not binary search identify is constarint for bs it is 10^5
##Pattern i observed is like it same as other heap we want some small/big +k what differnt is it usually cntains some 2 arrays or single 2D array like this.
"""Once again saying it requires sorting"""
#We have to combine two arrays are 2 d array and sort them maxx all cases
#These Type of problems start with brute force
#Then think greedily what I want like- Maximum hire k workers---i want to take workers with max ratio and qualities will be heaped
#                                      Maximum subsequence score--I want to maximize both sum and min but i will try to maximize min first and then on sum
#                                      Cousre Shedule--- I want to do tasks which end fastly
"""
######################For this problem you can use while or for loop must only to length of array nothing ever
"""
"""
Lets say about maximum subsequence score i.e i will have 2 arrays a=[1,2,2,3] b=[1,2,3,5] i want k=3 numbers from a and b (same indices)
ans=sum(k numbers from a)*min(k numbers from b)
#As usual 2 arrays combined into one [[1,1],[2,2],[2,3],[3,5]]
First i Will think to maximize minimum so descending sort based on b(for min)
                   [[3,5],[2,3],[2,2],[1,1]]
let say minimum      |This one so min=5  and sum=(_+_+3(curr index)) I want 2 more if I choose any elemnt on right my min will change because sorted 
                       So definately have to choose from left side of current index(Nothing can be choosen) change min
Now min                    |(still cant be choosen) sum=(_+2+3)
Now                              | so min=2 and sum=(3+2+2)all ans=14
Now min                                |  so min =1 and before adding current index i need to free something from sum
                                           I want to maximize sum so will remove small (MIN heap can used!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!)
                                           ans=1(min)*9(sum of top k with curr index)
Do understand better see code below
Same with hire minimum k workers  i have quality array=[2,3,4] min_wage=[9,1,1](min salary def paid) k=2 choose k workers so that ratio of quality and wage will give min salary
ratio=quality[i]/wage[i]=quality[j]/wage[j]
Take ratio=[2/9=0.2,3,4] Say if I choose worker=2(ratio 0.9) and choose worker(quality)=3 ratio(3) so i need to pay him amount as 0.9 times=1/0.9(formula)=0.0009 but min wage must be 1 so I can't choose worker=2
                         Choose worker=3(ratio 3) nxt 1)choose worker=2 his wage=2/3=0.6< his min_wage
                                                      2)Else choose worker=4 his wage=4/3=1.3>min_wage ans=3+1.3=4.3
                         Choose worker=4(ratio 4) nxt 1)Choose worker=2 his wage=2/4=0.5<min_wage
                                                      2)Choose worker=3 his wage=3/4=0.25<min_wage
From what observed ratio(larger) means better k choosing with minimum amount
So sort based on ratio,quality
                       [[0.2,2],[3,3],[4,4]]
#Let say i will def      |(choose this) k-1 small ratio nothing skip
                                  | choose(3,2)   ratio<min_wage skip
                                        | choose(3) and k-1 i want to choose with small quality so remove big one i.e 3(Max heap again!!!!!!!!!!!!!!!!!!!!!!!!)
                        This is answer like this you can find heaps minimum pattern
                        Optimize ==(quality1*large(ratio)+quality2*large(ratio))=ratio(quality1+quality2)
                        #This is optimization
"""
###########
"""
2542. Maximum Subsequence Score
You are given two 0-indexed integer arrays nums1 and nums2 of equal length n and a positive integer k. You must choose a subsequence of indices from nums1 of length k.
For chosen indices i0, i1, ..., ik - 1, your score is defined as:
The sum of the selected elements from nums1 multiplied with the minimum of the selected elements from nums2.
It can defined simply as: (nums1[i0] + nums1[i1] +...+ nums1[ik - 1]) * min(nums2[i0] , nums2[i1], ... ,nums2[ik - 1]).
Return the maximum possible score.
A subsequence of indices of an array is a set that can be derived from the set {0, 1, ..., n-1} by deleting some or no elements.

Example 1:
Input: nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3
Output: 12
Explanation: 
The four possible subsequence scores are:
- We choose the indices 0, 1, and 2 with score = (1+3+3) * min(2,1,3) = 7.
- We choose the indices 0, 1, and 3 with score = (1+3+2) * min(2,1,4) = 6. 
- We choose the indices 0, 2, and 3 with score = (1+3+2) * min(2,3,4) = 12. 
- We choose the indices 1, 2, and 3 with score = (3+3+2) * min(1,3,4) = 8.
Therefore, we return the max score, which is 12.
Example 2:
Input: nums1 = [4,2,3,1,1], nums2 = [7,5,10,9,6], k = 1
Output: 30
Explanation: 
Choosing index 2 is optimal: nums1[2] * nums2[2] = 3 * 10 = 30 is the maximum possible score.
 
Constraints:
n == nums1.length == nums2.length
1 <= n <= 105
0 <= nums1[i], nums2[j] <= 105
1 <= k <= n
"""
#Explain
"""
Lets say about maximum subsequence score i.e i will have 2 arrays a=[1,2,2,3] b=[1,2,3,5] i want k=3 numbers from a and b (same indices)
ans=sum(k numbers from a)*min(k numbers from b)
#As usual 2 arrays combined into one [[1,1],[2,2],[2,3],[3,5]]
First i Will think to maximize minimum so sort based on b
                   [[3,5],[2,3],[2,2],[1,1]]
let say minimum      |This one so min=5  and sum=(_+_+3(curr index)) I want 2 more if I choose any elemnt on right my min will change because sorted 
                       So definately have to choose from left side of current index(Nothing can be choosen) change min
Now min                    |(still cant be choosen) sum=(_+2+3)
Now                              | so min=2 and sum=(3+2+2)all ans=14
Now min                                |  so min =1 and before adding current index i need to free something from sum
                                           I want to maximize sum so will remove small (MIN heap can used!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!)
                                           ans=1(min)*9(sum of top k with curr index)
"""
#Answer 2 pass
from heapq import *
class Solution(object):
    def maxScore(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        #maximize minimum nums2
        #sort in desc based on nums2
        store=[[nums2[i],nums1[i]] for i in range(len(nums1))]
        store.sort(reverse=True)
        #I will consider one one value as minimum which is maximum
        #Okay one will be take what about remaining k-1 but i cant take from right else min will change nothing from left(in beginning) so first value cant be min
        #Atleast need to have k values and k will be min
        pq=[]
        m=-1 #my min 
        s=0 #sum
        for i in range(k):
            s+=store[i][1]
            m=store[i][0]
            heappush(pq,store[i][1])
        res=m*s 
        for i in range(k,len(nums1)):
            s+=store[i][1]
            #before adding next remove small one
            m=store[i][0]
            s-=heappop(pq)
            res=max(res,m*s)
        return res
#One pass(loops reduced to one)
class Solution(object):
    def maxScore(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        #maximize minimum nums2
        #sort in desc based on nums2
        store=[[nums2[i],nums1[i]] for i in range(len(nums1))]
        store.sort(reverse=True)
        pq=[]
        m=-1
        res=-1
        s=0
        for i in store:
            #add until k
            #after len==k check res
            #remove small --next iteration will work right
            if len(pq)==k:
                s-=heappop(pq)
            m=i[0]
            s+=i[1]
            heappush(pq,i[1])
            if len(pq)==k:
                res=max(res,m*s)
        return res
#Same format question  small differnce
"""
1383. Maximum Performance of a Team

You are given two integers n and k and two integer arrays speed and efficiency both of length n. There are n engineers numbered from 1 to n. speed[i] and efficiency[i] represent the speed and efficiency of the ith engineer respectively.
Choose at most k different engineers out of the n engineers to form a team with the maximum performance.
The performance of a team is the sum of its engineers' speeds multiplied by the minimum efficiency among its engineers.
Return the maximum performance of this team. Since the answer can be a huge number, return it modulo 109 + 7.

Example 1:
Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2
Output: 60
Explanation: 
We have the maximum performance of the team by selecting engineer 2 (with speed=10 and efficiency=4) and engineer 5 (with speed=5 and efficiency=7). That is, performance = (10 + 5) * min(4, 7) = 60.
Example 2:
Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3
Output: 68
Explanation:
This is the same example as the first but k = 3. We can select engineer 1, engineer 2 and engineer 5 to get the maximum performance of the team. That is, performance = (2 + 10 + 5) * min(5, 4, 7) = 68.
Example 3:
Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 4
Output: 72
"""
#Read question carfully atleast k so we can even have less<k elements
class Solution(object):
    def maxPerformance(self, n, speed, efficiency, k):
        """
        :type n: int
        :type speed: List[int]
        :type efficiency: List[int]
        :type k: int
        :rtype: int
        """
        store=[[efficiency[i],speed[i]] for i in range(n)]
        store.sort(reverse=True)
        pq=[]
        m=-1
        res=-1
        s=0
        for i in store:
            m=i[0]
            s+=i[1]
            heappush(pq,i[1])
            res=max(res,m*s)#Res must be done everytime because atleast k boom boom
            if len(pq)==k:
                res=max(res,m*s)
                s-=heappop(pq)
        return res
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
"""
Course Shedule III
There are n different online courses numbered from 1 to n. You are given an array courses where courses[i] = [durationi, lastDayi] indicate that the ith course should be taken continuously for durationi days and must be finished before or on lastDayi.
You will start on the 1st day and you cannot take two or more courses simultaneously.
Return the maximum number of courses that you can take.

Example 1:
Input: courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
Output: 3
Explanation: 
There are totally 4 courses, but you can take 3 courses at most:
First, take the 1st course, it costs 100 days so you will finish it on the 100th day, and ready to take the next course on the 101st day.
Second, take the 3rd course, it costs 1000 days so you will finish it on the 1100th day, and ready to take the next course on the 1101st day. 
Third, take the 2nd course, it costs 200 days so you will finish it on the 1300th day. 
The 4th course cannot be taken now, since you will finish it on the 3300th day, which exceeds the closed date.
Example 2:
Input: courses = [[1,2]]
Output: 1
Example 3:
Input: courses = [[3,2],[4,3]]
Output: 0

Constraints:
1 <= courses.length <= 104
1 <= durationi, lastDayi <= 104
"""
#Think this as task sheduling
#For example you have 3 tasks to do 1)use phone(5hr,within 10 hours) 2)eat (1 hr,within 7 hrs) 3)go to school(12 hr,within 13hr)
#Let say i go to school  it takes 12 hrs after i cant use phone/eat becuse time over
#So lets say instead of going to school eat because deadline 7 hrs complted hr=1 
#then use phone complte+phone hr=1+5=6 within 10 hours
#then go to school complete+school=6+12=18>deadline
####What will you do go to school(1 task) else do 2 tasks
''''''
#So for example i first did phone 5 hours then go to school 5+12=17<13(deadline) but cant eat(1 hour)
#So i will instead remove long time task and do this task okay but if the task I'm going to do takes more time than longest task which I did then nope i will never do it who will longest tasks
####So basically i will do fast tasks boom boom boom
class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        did=[]
        l=[[i[1],i[0]] for i in courses]
        l.sort()
        time=0
        for i in l:
            if time+i[1]<=i[0]:
                time+=i[1] #Doing tasks casually
                heappush(did,-i[1])
            elif did and -did[0]>i[1]:# i will only do if task takes less time than already done longest one
                time+=heappop(did)+i[1] #I wont do longest task instead i will now task which is small
                heappush(did,-i[1])
        return len(did)
