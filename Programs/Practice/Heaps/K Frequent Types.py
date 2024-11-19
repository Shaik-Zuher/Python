##Top freqent means biggest.
#########Heaps can be used on even strings i.e on frequencies of letters in string.
#basically some sort of frequency related things.
#heaps always need not to be numbers they can can be lists.
#[[0,"a"],[1,"b"],[2,"c"]] like this.
"""
In frequency-
for example create a string with following elements a=7,b=3,c=1 where all elements must be in string and 2 strings not beside
we starting building string with letter with most freq so we can create longest possible string
a->ab(because a already used next most freq)->aba(once again a) like this
if we create with other letter ex:c->cabababa(not all a used right so not possible and good).
So heap can have anything be it [freq,ele] or[diff,ele] anything....
"""
#hashmaps and heaps are also related seriouly hashmap related with lot of things man
"""
Top K Frequent in Array
Given a non-empty array arr[] of integers, find the top k elements which have the highest frequency in the array. If two numbers have the same frequencies, then the larger number should be given more preference.
Examples:
Input: k = 2, arr[] = [1, 1, 1, 3, 3, 4]
Output: [1, 3]
Explanation: Elements 1 and 3 have the same frequency ie. 2. Therefore, in this case, the answer includes the element 1 and 3.
"""
from heapq import heapify,heappop,heappush
from collections import Counter
class Solution:
	def topK(self,k, arr):
		pq=[]
		mp=Counter(arr)
		heapify(pq)
		#Top-biggest-min heap
		for i in mp.keys():
			ele=[mp[i],i]
			heappush(pq,ele)
			if len(pq)>k:
				heappop(pq)
		#our heap [[2,3],[3,1]] we want to print biggest element first -Convert to max heap
		for i in range(len(pq)):
			pq[i][0]*=-1
			pq[i][1]*=-1#neccesary becoz of ties
		heapify(pq)#Once again becoz strucure is broken when converted
		ans=[]
		while pq:
			ele=heappop(pq)
			ans.append(-ele[1])#change back
		return ans
"""
621. Task Scheduler
You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label.
Return the minimum number of CPU intervals required to complete all tasks.

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.
After completing task A, you must wait two intervals before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th interval, you can do A again as 2 intervals have passed.

Example 2:
Input: tasks = ["A","C","A","B","D","B"], n = 1
Output: 6
Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.
With a cooling interval of 1, you can repeat a task after just one other task.

Example 3:
Input: tasks = ["A","A","A", "B","B","B"], n = 3
Output: 10
Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.
There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.
"""		
from heapq import heapify,heappop,heappush
from collections import Counter,deque
#A -> B -> idle -> A -> B -> idle -> A -> idle->idle->A
#the element with most freq will be tasked first
class Solution:
    def leastInterval(self,tasks,K):
        # Code here
        mp=Counter(tasks)
        #mp={A:3,B:2}
        ans=[]
        heapify(ans)
        time=0
        blocked=deque([])
        for i in mp.keys():
            heappush(ans,[-mp[i],i])
        #ans=[[-4,A],[-2,B]]
        """
        ans=[[-3,A],[-2,B]] k=2
        time=1-task A is assigned so A need to be used 3 more times i.e [-3,A] but sholud be blocked until time =3
        blocked=[[3(time until block),A]]
        time=2-task B is assigned [-1,B] not it also blocked until time+k=4
        blocked=[[3,A],[4,B]] ans=[]
        time=3-Idle because now it is 3 so removed fom blocked and added to ans
        time=4-task A assigned blocked it time+k blocked=[[4,B],[6,A]] same time B will become free
        time=5-task B assigned now B=0 so no need blocked=[[6,A]] ans=[]
        time=6-idle now as 6 should be free blocked=[] ans=[[-2,A]]
        time=7-A assigned and blocked until time+k=9 blocked=[[9,A]]
        ###Now instead of waiting for time=9 as ans is already empty even after checking ###blocked timer## change time=blocked[0]-1 i.e to time 1 min before to blocked task so need of extra waiting
        time skipped to 8 
        when time=9 it becomes free and added thats all.....
        """
        while ans or blocked:
            time+=1
            if ans:
                c=heappop(ans)
                #most freq task is removed and will be blocked for next k sec i.e(curr time+k)
                c[0]+=1
                if(c[0]<0):
                    blocked.append([time+K,c])
            if blocked and blocked[0][0]<=time:#when time reached then removed
                heappush(ans,blocked.popleft()[1])
            if not ans and blocked:#for example ans empty and to reduce time complexity lets change time to first blockrd task-1
                time+=((blocked[0][0]-time)-1)
            #print(ans,blocked,time)
        return time		
		
