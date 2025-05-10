"""
Miniumum number of rooms
Mininum number of times room used

These are 2 types of mins
"""
#Minimum room is type such thatyou will have n meetings and tell mininum number of rooms to conduct meetings
#Yeah this is same heap type where keepu adding meeting to heap when adding meeting check if smallest meeting is ending
#Minimum number if rooms,Mininum number of platforms this type
""""""
#Another type says like max number of meetings held in single room -Like N meetings held in single room
"""
N meetings in one room
You are given timings of n meetings in the form of (start[i], end[i]) where start[i] is the start time of meeting i and end[i] is the finish time of meeting i. Return the maximum number of meetings that can be accommodated in a single meeting room, when only one meeting can be held in the meeting room at a particular time. 

Note: The start time of one chosen meeting can't be equal to the end time of the other chosen meeting.
Examples :

Input: start[] = [1, 3, 0, 5, 8, 5], end[] =  [2, 4, 6, 7, 9, 9]
Output: 4
Explanation: Maximum four meetings can be held with given start and end timings. The meetings are - (1, 2), (3, 4), (5,7) and (8,9)
Input: start[] = [10, 12, 20], end[] = [20, 25, 30]
Output: 1
Explanation: Only one meetings can be held with given start and end timings.
"""
#Brute sort both mixed then 2 loops like consider first meeting(first loop) and keep checking remaining meeting if start<end(2nd loop)
#Tracking max at end
##Hmmmm what can we do greedy if will take meeting which end first and then keep adding next fast ending rooms
class Solution:
    def maximumMeetings(self,start,end):
        store=[[end[i],start[i]] for i in range(len(start))]
        store.sort()###Which ends first
        ans=1#first room
        prev=store[0][0]
        for i in range(1,len(store)):
            if(prev<store[i][1]):
                ans+=1
                prev=store[i][0]
        return ans
