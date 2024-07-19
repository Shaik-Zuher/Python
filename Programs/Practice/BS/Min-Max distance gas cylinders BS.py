###############################################Minimise Maximum Distance between Gas Stations#######################################
"""
Problem Statement: You are given a sorted array ‘arr’ of length ‘n’, which contains positive integer positions of ‘n’ gas stations on the X-axis.
You are also given an integer ‘k’. You have to place 'k' new gas stations on the X-axis.
You can place them anywhere on the non-negative side of the X-axis, even on non-integer positions.
Let 'dist' be the maximum value of the distance between adjacent gas stations after adding k new gas stations.
Find the minimum value of ‘dist’.
Note: Answers within 10^-6 of the actual answer will be accepted.
For example, if the actual answer is 0.65421678124, it is okay to return 0.654216.
Our answer will be accepted if that is the same as the actual answer up to the 6th decimal place.
Examples
Example 1:
Input Format:
 N = 5, arr[] = {1,2,3,4,5}, k = 4
Result:
 0.5
Explanation:
 One of the possible ways to place 4 gas stations is {1,1.5,2,2.5,3,3.5,4,4.5,5}.
 Thus the maximum difference between adjacent gas stations is 0.5.
 Hence, the value of ‘dist’ is 0.5.
 It can be shown that there is no possible way to add 4 gas stations in such a way that the value of ‘dist’ is lower than this. 
Example 2:
Input Format:
 N = 10, arr[] = {1,2,3,4,5,6,7,8,9,10}, k = 1
Result:
 1
Explanation:
 One of the possible ways to place 1 gas station is {1,1.5,2,3,4,5,6,7,8,9,10}.
 Thus the maximum difference between adjacent gas stations is still 1.
 Hence, the value of ‘dist’ is 1.
 It can be shown that there is no possible way to add 1 gas station in such a way that the value of ‘dist’ is lower than this.
 """
"""#########################################################################################################################################
   12  13 14 16 and k=1
dif   1  1  2  we want minimum distance which is max so lets place k in btween 14 and 16
now every ditsnace has distance 1 so min distance will be 1 this mechanism will be used during condition check
"""
import math
N = 5
arr= [1,2,3,4,5]
k = 4
def bs(N,arr,k):
    def condition(mid):
        nplaced=0
        for i in range(1,N): ##############some mind calc 12   17 have greatest distance lets think we need to minimize that 
            distance=(arr[i]-arr[i-1])/mid       ################# how many stations can be added to minimize it.Lets say mid=2 and if we place one station
                            ################# 12   15   17 still differnce is 3 so lets place 1 more  so totally 2 stations are place now how to  get this 2
                                              #  3    2    diff  can we get by math.ceil(dst/mid)
                                              #but this case has problems with some cases ie if 4 stations are placed
                                              # 12   17
                                              # 12 13 14 15 16 17 mid=1
                                              #math.ceil(5/1)=1 so it wont work on cases which has no fraction part so -1 during these parts
            # here if(>mid ) not used becuase  lets say 1 2 5 6 we place gas stations between all points regarding of dist
            if arr[i]-arr[i-1]==distance*mid: #this will check that -1 condition
                nplaced-=1
            nplaced+=distance
        return nplaced<=k
                
    s=0
    e=0
    for i in range(N-1):
        e=max(e,arr[i+1]-arr[i])
        #unlike agressive cows we are placing stations bewteen already existin stations raed carefully ufff
    while e-s>1e-6:#####let say 0.5 is answer but 0.0000000000456 can also be answer  and 0.00000000000000000000455 can also be answer which can create a infinite
        mid=s+(e-s)/2    #####to prevent this question given to keep answer between 0.0000001 so lets keep it as condition
        if(condition(mid)):
            e=mid###not to miss decimals
        else:
            s=mid
    return e
print(bs(N,arr,k))
def isPossible(stations, mid, k):
    total = 0
    for i in range(1, len(stations)):
        dis = stations[i] - stations[i - 1]
        total+=math.ceil(dis/mid) - 1
    return total<= k

def dist(stations, k):
    n = len(stations)
    low, high = 0, stations[n - 1] - stations[0]
    ans = high
    while high - low >= 1e-6:
        mid = (low + high) / 2
        if isPossible(stations, mid, k):
            ans = mid
            high = mid
        else:
            low = mid
    return ans
print(dist(arr,k))
